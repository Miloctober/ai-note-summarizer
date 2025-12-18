# Summarization Module (Dev 1)

## Your Job
You are responsible for implementing the text summarization functionality. This module takes raw lecture notes or documents and extracts key information.

## What You Need to Implement

### `summarizer.py` - `Summarizer` class

**Method: `summarize(text: str) -> SummaryOutput`**

Your task is to:
1. Take the input `text` parameter (raw lecture notes or document)
2. Generate a comprehensive summary paragraph
3. Extract 3-5 key bullet points
4. Identify 5-10 key concepts/terms from the text
5. Track the original text length
6. Measure how long processing took
7. Return all this in a `SummaryOutput` object

**Example output:**
```python
SummaryOutput(
    summary="This lecture discusses quantum mechanics principles...",
    bullet_points=["Principle 1", "Principle 2", "Principle 3"],
    key_concepts=["Quantum Mechanics", "Wave Function", "Superposition"],
    text_length=2500,
    processing_time=0.45
)
```

## What You CAN Do
- ✅ Modify anything inside `src/summarization/`
- ✅ Add helper functions or classes in this module
- ✅ Import external libraries (with team approval)
- ✅ Add tests specific to summarization
- ✅ Use industry-standard NLP libraries (e.g., transformers, spacy, nltk)

## What You CANNOT Do
- ❌ Modify `src/quiz/` or `src/web/`
- ❌ Change the `SummaryOutput` dataclass structure
- ❌ Change the method signature of `summarize()`
- ❌ Modify files outside your module without team discussion

## Integration Points
- Your `SummaryOutput` is consumed by `src/web/app.py` 
- The `WebApp.process_text()` method will call your `Summarizer.summarize()` method
- Make sure your output matches the defined `SummaryOutput` structure exactly

## Testing
Write your tests in `tests/test_summarization.py`

Test your implementation with:
```bash
pytest tests/test_summarization.py
```

## Dependencies
If you need to add a new package:
1. Create an issue describing why
2. Get team approval
3. Update `requirements.txt`
4. Everyone installs: `pip install -r requirements.txt`

## Questions?
Check `src/summarization/models.py` to see the exact structure of `SummaryOutput`.
