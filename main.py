from utils import expand_abbreviation
import pandas as pd

print("💬 Bank Name Expander — Type an abbreviation or 'quit'")

while True:
    query = input("Enter an abbreviated bank name (or 'quit'): ").strip()
    if query.lower() == 'quit':
        print("Goodbye!")
        break

    matches = expand_abbreviation(query, top_k=3, threshold=0.25)
    if matches:
        for name, score in matches:
            print(f"{name} (score: {round(score, 4)})")
    else:
        print("❌ No confident match found.")
    print("---")
