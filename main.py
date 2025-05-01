import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample full names to match against (expand this list)
full_names = [
    "Bank of America", "Wells Fargo", "Citigroup", "Goldman Sachs",
    "JPMorgan Chase", "Morgan Stanley", "Barclays", "HSBC",
    "Deutsche Bank", "Capital One", "American Express", "Chase Bank"
]

# Precompute full name embeddings
full_name_embeddings = model.encode(full_names)

def expand_abbreviation(user_input, top_k=3):
    input_embedding = model.encode([user_input])
    similarities = cosine_similarity(input_embedding, full_name_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    results = [(full_names[i], round(similarities[i], 4)) for i in top_indices]
    return results

if __name__ == "__main__":
    while True:
        query = input("Enter an abbreviated bank name (or 'quit'): ").strip()
        if query.lower() == 'quit':
            break
        matches = expand_abbreviation(query)
        for name, score in matches:
            print(f"{name} (score: {score})")
        print("---")
