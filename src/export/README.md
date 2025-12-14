# Web Interface Module (Dev 3)

## Your Job
You are responsible for exporting the data (summary and quiz) in multiple formats: pdf, flashcards on Anki

## What You Need to Implement!

### `exportation.py`

**Method 1: `export_results(summary: SummaryOutput, quiz: QuizOutput, format: str) -> str`**

Your task is to:
1. Take the summary and quiz outputs
2. Take a format parameter (e.g., "pdf", "json", "html")
3. Convert the results to the requested format
4. Save or return the formatted output
5. Support multiple export formats

**Example usage:**
```python
app = WebApp()
results = app.process_text("Input text here...")
file_path = app.export_results(results['summary'], results['quiz'], 'pdf')
```

## What You CAN Do
- ✅ Modify anything inside `src/web/`
- ✅ Add helper functions or classes for UI/export logic
- ✅ Import web frameworks (Flask, FastAPI, Django, etc.) - with team approval
- ✅ Add export format handlers (PDF, JSON, HTML, etc.)
- ✅ Create the actual web interface/frontend
- ✅ Add tests specific to the web interface

## What You CANNOT Do
- ❌ Modify `src/summarization/` or `src/quiz/`
- ❌ Change the `WebApp` method signatures
- ❌ Change how `Summarizer` or `QuizGenerator` work
- ❌ Modify the input/output structures (SummaryOutput, QuizQuestion, QuizOutput)

## Dependencies You'll Use
- The `Summarizer` class from `src.summarization`
- The `QuizGenerator` class from `src.quiz`
- The output dataclasses: `SummaryOutput`, `QuizQuestion`, `QuizOutput`

## What Comes In
```
Input: Raw text from user
       ↓
       Summarizer.summarize() → SummaryOutput
       ↓
       QuizGenerator.generate() → QuizOutput
       ↓
```

## What Goes Out
```
       Display summary, bullets, concepts
       Display quiz questions with options
       Export options (PDF, JSON, HTML, etc.)
       ↓
Output: Formatted file or display
```

## Testing
Write your tests in `tests/test_web.py`

Test your implementation with:
```bash
pytest tests/test_web.py
```

## Integration Notes
- Dev 1's `Summarizer` will already be working when you integrate
- Dev 2's `QuizGenerator` will already be working when you integrate
- You just need to call them and display/export the results
- Don't worry about their implementation details

## Questions?
- See `src/summarization/models.py` for `SummaryOutput` structure
- See `src/quiz/models.py` for `QuizQuestion` and `QuizOutput` structures
- Check how the Summarizer and QuizGenerator are initialized in the `WebApp.__init__()`
