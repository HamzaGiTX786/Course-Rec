import fitz
import faiss
import numpy as np
from openai import OpenAI
from nltk import download
from nltk.tokenize import sent_tokenize
import pickle
import os
from coursrec import settings

download("punkt")  # For sentence tokenizer

client = OpenAI()
client.api_key = settings.OPENAI_API_KEY

def process_pdf_to_faiss(pdf_path, index_path="rag_index.index", meta_path="rag_meta.pkl"):

    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)

    # Create FAISS index
    dim = len(embeddings[0][1])
    index = faiss.IndexFlatL2(dim)
    texts = []

    for chunk_text_context, embedding in embeddings:
        index.add(np.array([embedding]))
        texts.append(chunk_text_context)

    # Save index and metadata
    faiss.write_index(index, index_path)
    with open(meta_path, 'wb') as f:
        pickle.dump(texts, f)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def chunk_text(text, max_tokens=300):
    sentences = sent_tokenize(text)
    chunks, current_chunk, current_length = [], [], 0
    for sentence in sentences:
        tokens = sentence.split()
        if current_length + len(tokens) > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(sentence)
        current_length += len(tokens)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def get_embeddings(chunks):
    vectors = []
    for chunk in chunks:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        vectors.append((chunk, np.array(response.data[0].embedding, dtype='float32')))
    return vectors
