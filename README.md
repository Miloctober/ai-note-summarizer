# AI Note Summarizer

An intelligent tool that transforms lecture notes into summaries, bullet points, key concepts, and quizzes using AI.


## 📁 Project Structure

```
ai-note-summarizer/
├── src/
│   ├── __init__.py
│   ├── cli/                    # CLI: Command-line interface
│   │   └── __init__.py
│   ├── export/                 # Export Module
│   │   └── __init__.py
│   ├── summarization/          # Summarization Module
│   │   ├── __init__.py
│   │   ├── summarizer.py
│   │   └── models.py
│   ├── quiz/                   # Quiz Generation Module
│   │   ├── __init__.py
│   │   ├── generator.py
│   │   └── models.py
│   ├── web/                    # Web Interface (Flask/Streamlit)
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── routes.py
│   └── utils/                  # Shared utilities
│       ├── __init__.py
│       ├── text_processing.py
│       └── export.py
├── tests/
│   ├── __init__.py
│   ├── test_summarization.py
│   ├── test_quiz.py
│   └── test_integration.py
│
├── config/
│   ├── config.py               # Configuration settings
│   └── settings.example.py     # Example settings
│
├── main.py                     # Entry point
├── requirements.txt            # Dependencies
├── .gitignore
├── README.md
└── DEVELOPMENT.md              # Dev guidelines
```

## 🚀 Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd ai-note-summarizer

# Install dependencies

pip install -r requirements.txt

# Run the web app
python -m src.web.app
```

## 📋 Requirements

- Python 3.9+
- See `requirements.txt` for full list

## 🔗 Integration Points

All modules communicate through standardized interfaces in `models.py`:

1. **Summarizer** → Returns `SummaryOutput`
2. **Quiz Generator** → Returns `QuizOutput`
3. **Web Interface** → Calls both modules and displays results
4. **Utils** → Used by all modules for common tasks



