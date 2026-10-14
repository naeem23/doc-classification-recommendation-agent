from dataclasses import dataclass
from datetime import datetime
import numpy as np
from core.storage.models import DocumentRecord, ClassCentroidRecord

def _to_bytes(vec) -> bytes:
    return np.asarray(vec, dtype=np.float32).tobytes()

def _to_vec(data: bytes) -> np.ndarray:
    return np.frombuffer(data, dtype=np.float32)

@dataclass
class StoredDocument:
    id: int
    filename: str
    class_name: str | None
    source: str | None 
    url: str | None 
    created_at: datetime 
    embedding: np.ndarray

@dataclass
class StoredCentroid:
    class_name: str 
    doc_count: int 
    embedding: np.ndarray


class Repository:
    def __init__(self, session_factory):
        self._session_factory = session_factory

    def save_document(self, filename, embedding, class_name=None, source=None, url=None):
        with self._session_factory() as session:
            session.add(DocumentRecord(
                filename=filename,
                class_name=class_name,
                source=source,
                url=url,
                embedding=_to_bytes(embedding)
            ))
            session.commit()

    def save_centroid(self, class_name, embedding, doc_count):
        with self._session_factory() as session:
            record = session.query(ClassCentroidRecord).filter_by(class_name=class_name).first()
            if record is None:
                session.add(ClassCentroidRecord(
                    class_name=class_name,
                    doc_count=doc_count,
                    embedding=_to_bytes(embedding)
                ))
            else:
                record.doc_count = doc_count
                record.embedding = _to_bytes(embedding)

            session.commit()

    def get_all_documents(self) -> list[StoredDocument]:
        with self._session_factory() as session:
            return [
                StoredDocument(r.id, r.filename, r.class_name, r.source, r.url, r.created_at, _to_vec(r.embedding))
                for r in session.query(DocumentRecord).all()
            ]

    def get_all_centroids(self) -> list[StoredCentroid]:
        with self._session_factory() as session:
            return [
                StoredCentroid(r.class_name, r.doc_count, _to_vec(r.embedding))
                for r in session.query(ClassCentroidRecord).all()
            ]

        