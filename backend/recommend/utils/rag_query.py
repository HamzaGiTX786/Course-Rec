import numpy as np
import pickle
import faiss
from openai import OpenAI
from coursrec import settings

client = OpenAI()
client.api_key = settings.OPENAI_API_KEY

def retrieve_top_k_chunks(query, k=3, index_path="rag_index.index", meta_path="rag_meta.pkl"):
    # Load index and metadata
    index = faiss.read_index(index_path)
    with open(meta_path, 'rb') as f:
        texts = pickle.load(f)

    # Embed query
    query_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding
    query_vector = np.array([query_embedding], dtype='float32')

    # Search
    distances, indices = index.search(query_vector, k)
    return [texts[i] for i in indices[0]]
