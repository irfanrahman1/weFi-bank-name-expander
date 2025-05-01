
# weFi Bank Name Expander

This is a simple AI tool that takes short or abbreviated bank names (like "CITI" or "BOFA") and tries to guess their full names (like "Citigroup" or "Bank of America"). It uses a small open-source language model to compare meanings and find the best matches.

---

## 🔍 What It Does

- You type an abbreviation (like `FLORIDASTACU`)
- It shows you the top 3 full bank names it thinks are the best match
- It shows a score for each match (higher means more likely)

---

## 🧠 How It Works

- Uses the `all-MiniLM-L6-v2` model from SentenceTransformers
- Compares your input with a list of real bank names
- Uses cosine similarity to find the most similar matches

---

## 🛠️ How to Use It

1. Make sure you have Python installed
2. Install the required packages:
   ```
   pip install sentence-transformers scikit-learn pandas
   ```
3. Run the code:
   ```
   python main.py
   ```
4. Type in a bank abbreviation and press Enter

---

## 📋 Example

```
Enter an abbreviated bank name (or 'quit'): FLORIDASTACU
Bank of America (score: 0.2977)
Wells Fargo (score: 0.2729)
HSBC (score: 0.2668)
---
```

---

## ⚠️ Current Limitations

- Only uses a small list of ~12 banks for now
- Doesn’t understand abbreviation rules (like breaking up capital letters)
- Might guess wrong if the abbreviation is uncommon or messy

---

## ✅ What Could Be Better

- Add more real bank names from the CSV file
- Handle weird or unclear inputs better
- Build a simple website or button-based version
- Use a smarter system like fine-tuning or abbreviation-specific logic
