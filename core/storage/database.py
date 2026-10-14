from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.storage.models import Base

def create_session_factory(db_url: str = "sqlite:///data.db"):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)