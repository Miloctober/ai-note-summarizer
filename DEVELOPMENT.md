# Development Guidelines for Team Collaboration

## 🎯 How to Avoid Conflicts

### 1. **Each Developer Works in Their Own Module**
- **Yujin**: Only modifies `src/summarization/`
- **Layaanee**: Only modifies `src/quiz/`
- **Dev 3**: Only modifies `src/web/`
- **Dev 4**: Only modifies `tests/` and docs

### 2. **Shared Code Lives in Specific Places**
- **Config**: `config/config.py` (discuss changes in team)
- **Utils**: `src/utils/` (create new functions, don't delete)
- **Models/Interfaces**: `src/[module]/models.py` (define contracts here)

### 3. **Never Modify**
- Other developers' module files
- `main.py` without team discussion
- `requirements.txt` without approval

### 4. **How to Add Dependencies**
1. Create an issue describing why you need it
2. Team agrees on the package
3. ONE person adds to `requirements.txt`
4. Everyone does `pip install -r requirements.txt`

## 📦 Module Interfaces (Contracts)

### Dev 1: Summarization Module
**File**: `src/summarization/models.py`
```python
from dataclasses import dataclass

@dataclass
class SummaryOutput:
    summary: str           # Main summary paragraph
    bullet_points: list    # List of key points
    key_concepts: list     # List of terms/concepts
    text_length: int       # Original text length
    processing_time: float # How long it took
```

### Dev 2: Quiz Module
**File**: `src/quiz/models.py`
```python
from dataclasses import dataclass
from typing import List

@dataclass
class QuizQuestion:
    question: str
    answer: str
    options: List[str]  # 4 multiple choice options
    difficulty: str     # "easy", "medium", "hard"

@dataclass
class QuizOutput:
    questions: List[QuizQuestion]
    total_questions: int
    source_text: str
```

### Dev 3: Web Interface
**File**: `src/web/app.py`
- Takes text input from user
- Calls `Summarizer.summarize(text)` → gets `SummaryOutput`
- Calls `QuizGenerator.generate(text)` → gets `QuizOutput`
- Displays results and export options

## 🔧 Workflow

### Daily Workflow
```bash
# Start your shift
git pull origin main

# Make your changes in your module
# Edit only files in src/[your_module]/

# Test your changes
python -m pytest tests/test_[your_module].py

# Commit with clear messages
git add src/[your_module]/
git commit -m "Dev X: [what you did]"

# Push when ready
git push origin main
```

### Before Making a Pull Request
1. Run all tests: `pytest`
2. No merge conflicts
3. Code is documented
4. Interfaces are honored

## 📝 Code Standards

### Naming Convention
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

### Documentation
Every function needs a docstring:
```python
def summarize(text: str) -> SummaryOutput:
    """
    Generate a summary from input text.
    
    Args:
        text: Raw lecture notes or document text
        
    Returns:
        SummaryOutput with summary, bullets, and concepts
        
    Raises:
        ValueError: If text is empty or too short
    """
```

### Testing
- Write tests for your module in `tests/test_[your_module].py`
- Run tests before pushing: `pytest tests/`
- Aim for >80% code coverage

## 🚨 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Import errors | Make sure `__init__.py` files exist |
| Merge conflicts | Pull latest, resolve in your editor, test |
| Unsure about interface | Check `src/[module]/models.py` for the contract |
| Need to call another module | Use the standard interface from `models.py` |
| Different versions of packages | Everyone install from `requirements.txt` |

## 🔄 Integration Testing

Dev 4 is responsible, but here's the flow:
1. Summarizer extracts text → `SummaryOutput`
2. Quiz Generator reads extracted text → `QuizOutput`
3. Web app displays both outputs
4. Export functionality works for both

## 📚 Useful Commands

```bash
# Install everything
pip install -r requirements.txt

# Run all tests
pytest

# Run specific module tests
pytest tests/test_summarization.py

# Check code style
black src/

# Format code
black src/ --check
```

## ✍️ Commit Message Format

```
[Dev X] Brief description

Longer explanation if needed.
- Bullet point 1
- Bullet point 2

Fixes #123 (if relevant)
```

## 🎉 You're Good to Go!

Start coding your module. If you get stuck, check the models/interfaces first!
