# AI Note Summarizer + Quiz Generator

An intelligent tool that transforms lecture notes into summaries, bullet points, key concepts, and quizzes using AI.

## 👥 Team Workflow

### Developer Responsibilities

| Developer | Module | Files | Status |
|-----------|--------|-------|--------|
| **Yujin** | Summarization | `src/summarization/` | To Do |
| **LAYAANEE** | Quiz Generation | `src/quiz/` | Done! |
| **Evan** | Web Interface | `src/web/` | To Do |
| **Milo** | Testing & Docs | `tests/`, `docs/` | To Do |
| **Milo** | Export Summary and Quiz | `export/`| To Do |
| **Dev 6** | Video transcription for Mediaserver | `transcript/`| To Do |
| **Dev 7** | Ask AI about your notes | `askai/`| To Do |
| **Dev 8** | Database with SQL and json? | `database/`| To Do |
| **LAYAANEE** | Conversion en long string (depuis transcription, polycopié ou slide) | `tolongstring/`| To Do |



## 📁 Project Structure

```
ai-note-summarizer/
├── src/
│   ├── __init__.py
│   │
│   ├── export/                 # Dev 5: Export Module
│   │   └── __init__.py
│   │
│   ├── summarization/          # Dev 1: Summarization Module
│   │   ├── __init__.py
│   │   ├── summarizer.py       # Main summarization logic
│   │   └── models.py           # Interfaces/base classes
│   │
│   ├── quiz/                   # Dev 2: Quiz Generation Module
│   │   ├── __init__.py
│   │   ├── generator.py        # Main quiz generation logic
│   │   └── models.py           # Interfaces/base classes
│   │
│   ├── web/                    # Dev 3: Web Interface
│   │   ├── __init__.py
│   │   ├── app.py              # Main Flask/Streamlit app
│   │   └── routes.py           # API endpoints
│   │
│   └── utils/                  # Shared utilities
│       ├── __init__.py
│       ├── text_processing.py  # Common text functions
│       └── export.py           # Export to PDF/TXT
│
├── tests/                      # Dev 4: Testing & Docs
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
python main.py
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

## ✅ Definition of Done

- ✅ Code follows project conventions
- ✅ Tests written and passing
- ✅ Module interfaces implemented
- ✅ Documentation updated
- ✅ No merge conflicts

## 📞 Communication

Use GitHub Issues and Pull Requests for coordination. Each developer works on their module independently.

---

**Last Updated**: December 2025
