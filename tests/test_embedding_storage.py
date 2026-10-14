import numpy as np
from core.embedding.local_model import LocalEmbeddingModel
from core.storage.database import create_session_factory
from core.storage.repository import Repository

def test_embed_save_load(tmp_path):
    model = LocalEmbeddingModel()
    repo = Repository(create_session_factory(f"sqlite:///{tmp_path / 'test.db'}"))

    vec = model.embed("Football match results")
    repo.save_document("a.txt", vec, class_name="Sports")

    docs = repo.get_all_documents()
    assert len(docs) == 1
    assert np.allclose(docs[0].embedding, vec)

def test_centroid_upsert(tmp_path):
    repo = Repository(create_session_factory(f"sqlite:///{tmp_path / 'test.db'}"))
    repo.save_centroid("Sports", np.ones(4), 2)
    repo.save_centroid("Sports", np.zeros(4), 5)

    centroids = repo.get_all_centroids()
    assert len(centroids) == 1
    assert centroids[0].doc_count == 5