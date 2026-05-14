import faiss
import numpy as np

index = faiss.IndexFlatL2(384)

stored_chunks = []

def store_embeddings(embeddings, chunks):

    global stored_chunks

    embeddings = np.array(embeddings).astype('float32')

    index.add(embeddings)

    stored_chunks = chunks

def search(query_embedding, k=3):

    query_embedding = np.array([query_embedding]).astype('float32')

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        results.append(stored_chunks[idx])

    return results