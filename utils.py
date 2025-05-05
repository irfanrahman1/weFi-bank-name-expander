from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# List of known bank names (expandable)
full_names = [
    "Bank of America", "Wells Fargo", "Citigroup", "Goldman Sachs",
    "JPMorgan Chase", "Morgan Stanley", "Barclays", "HSBC",
    "Deutsche Bank", "Capital One", "American Express", "Chase Bank"
]

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')
full_name_embeddings = model.encode(full_names)

def expand_abbreviation(user_input, top_k=3, threshold=0.5):
    input_cleaned = user_input.strip()
    input_embedding = model.encode([input_cleaned])
    similarities = cosine_similarity(input_embedding, full_name_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = [(full_names[i], float(similarities[i])) for i in top_indices if similarities[i] >= threshold]
    return results
