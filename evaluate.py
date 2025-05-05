import pandas as pd
from utils import expand_abbreviation

# Load the CSV file
df = pd.read_csv("Sample of unparsed bank names.csv")

print("📄 Sample data:")
print(df.head())

print("\n🔍 Testing sample predictions:")

# Adjust to use correct column if needed
for abbreviation in df.iloc[:10, 0]:  # first 10 rows from first column
    print(f"\nInput: {abbreviation}")
    matches = expand_abbreviation(abbreviation, top_k=2, threshold=0.25)
    if matches:
        for name, score in matches:
            print(f"→ {name} (score: {round(score, 4)})")
    else:
        print("→ ❌ No confident match found.")
