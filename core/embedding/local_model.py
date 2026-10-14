import numpy as np
from sentence_transformers import SentenceTransformer
from core.embedding.base import EmbeddingModel

class LocalEmbeddingModel(EmbeddingModel):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self._model = SentenceTransformer(model_name)

    def embed(self, text: str) -> np.ndarray:
        return self._model.encode(text).astype(np.float32)