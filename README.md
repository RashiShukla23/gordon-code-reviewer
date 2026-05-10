# Gordon — AI Code Reviewer

Gordon is an AI code reviewer that reads your code and gives honest, detailed feedback — bugs, bad practices, and concrete suggestions for improvement. No sugar-coating.

---

## What it does

- Spots bugs, edge cases, and potential runtime errors
- Reviews code structure, readability, and best practices
- Gives specific improvement suggestions, not generic advice
- Uses a consistent "Gordon" persona — a blunt senior developer

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | GPT-4.1 (OpenAI) |
| Agent Framework | LangGraph |
| Frontend | Streamlit + HTML/CSS |
| Language | Python |

---

## Project Structure

```
gordon-code-reviewer/
├── app.py        # Streamlit UI
├── graph.py      # LangGraph review pipeline
├── style.css     # Custom UI styling
└── .gitignore
```

---

## Getting Started

Prerequisites: Python 3.10+, OpenAI API key

```bash
git clone https://github.com/RashiShukla23/gordon-code-reviewer.git
cd gordon-code-reviewer

py -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_key
```

```bash
streamlit run app.py
```

---

## How it works

You paste your code into the text area, optionally specify the language and what to focus on, and Gordon runs it through a LangGraph review pipeline. The output covers bugs found, quality issues, and a corrected version where needed.

---

## Example

Input:
```python
def divide(a, b):
    return a / b
```

Gordon's review:
```
Bug: No handling for division by zero. This will raise a ZeroDivisionError at runtime.

Quality: Missing type hints and docstring.

Fix:
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

## Author

**Rashi Shukla** — [GitHub](https://github.com/RashiShukla23)
