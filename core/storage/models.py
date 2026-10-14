from datetime import datetime, timezone
from sqlalchemy import String, Integer, LargeBinary, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

def _now():
    return datetime.now(timezone.utc)

class DocumentRecord(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(String)
    class_name: Mapped[str | None] = mapped_column(String, nullable=True)
    source: Mapped[str | None] = mapped_column(String, nullable=True)
    url: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_now)
    embedding: Mapped[bytes] = mapped_column(LargeBinary)

class ClassCentroidRecord(Base):
    __tablename__ = "class_centroids"
    id: Mapped[int] = mapped_column(primary_key=True)
    class_name: Mapped[str] = mapped_column(String, unique=True)
    doc_count: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_now)
    embedding: Mapped[bytes] = mapped_column(LargeBinary)