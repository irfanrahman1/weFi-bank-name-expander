
# 🏦 Bank Name Expander — weFi Data Science Intern Project

This project builds a lightweight AI agent that takes an **abbreviated bank or financial service name** (e.g., `BOA`, `AMEX`) and generates the **corresponding full name** (e.g., `Bank of America`, `American Express`) using open-source language models.

---

## 🔍 Project Goals

✅ Build an AI agent using one or more open-source LLMs  
✅ Input: Abbreviated bank name  
✅ Output: Most likely full name  
✅ Evaluate using real-world data (provided CSV)  
✅ Demonstrate model usage, data handling, and understanding of limitations

---

## 🛠️ How It Works

- Uses the `all-MiniLM-L6-v2` model from SentenceTransformers to compute embeddings
- Matches user input to known bank names using **cosine similarity**
- Supports real-time user queries (`main.py`) and batch evaluation on a CSV dataset (`evaluate.py`)
- Filters low-confidence matches to avoid false positives

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `main.py` | Interactive script for real-time user input and matching |
| `utils.py` | Core logic: loads model, encodes input, returns top matches |
| `evaluate.py` | Evaluates model performance on sample abbreviations from CSV |
| `Sample of unparsed bank names.csv` | Provided sample data for testing |
| `requirements.txt` | Python dependencies |

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run interactive user input
```bash
python main.py
```

### 3. Run evaluation on sample CSV
```bash
python evaluate.py
```

---

## 💡 Example Predictions

```
Input: BOA
→ Bank of America (score: 0.369)

Input: AMEX
→ American Express (score: 0.6537)

Input: CITI
→ Citigroup (score: 0.6977)

Input: WEBBNKFSTR
→ ❌ No confident match found
```

---

## 📈 Limitations

- Lower confidence for **very short or obscure abbreviations**
- Model not fine-tuned on banking data
- Small set of known full names (can be expanded)

---

## 🔧 Ideas for Improvement

- Integrate a **manual abbreviation dictionary fallback**
- Use a larger full name list from the CSV or open datasets
- Fine-tune the transformer on domain-specific text
- Log prediction accuracy using labeled data

---

## 📬 Author

**Irfan Rahman**  
For the weFi Junior Data Scientist internship project, 2025  
