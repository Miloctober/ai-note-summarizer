# Quiz Generator Module (Dev 2)

## Your Job
You are responsible for generating quiz questions from input text. This module reads documents/lecture notes and creates multiple-choice questions to test understanding.

## What You Need to Implement

### `generator.py` - `QuizGenerator` class

**Method: `generate(text: str) -> QuizOutput`**

Your task is to:
1. Take the input `text` parameter (raw lecture notes or document)
2. Create multiple quiz questions based on the content
3. For each question, provide:
   - The question text
   - The correct answer
   - 4 multiple-choice options (including the correct answer mixed in)
   - A difficulty level ("easy", "medium", or "hard")
4. Count the total number of questions generated
5. Store the source text for reference
6. Return all this in a `QuizOutput` object

**Example output:**
```python
QuizOutput(
    questions=[
        QuizQuestion(
            question="What is quantum superposition?",
            answer="The state where particles exist in multiple states simultaneously",
            options=[
                "The state where particles exist in multiple states simultaneously",
                "When particles move very fast",
                "A property of light only",
                "The collapse of wave functions"
            ],
            difficulty="medium"
        ),
        # ... more questions
    ],
    total_questions=5,
    source_text="The original input text..."
)
```

## What You CAN Do
- ✅ Modify anything inside `src/quiz/`
- ✅ Add helper functions or classes in this module
- ✅ Import external libraries (with team approval)
- ✅ Add tests specific to quiz generation
- ✅ Use NLP/ML libraries for question generation (transformers, spacy, etc.)

## What You CANNOT Do
- ❌ Modify `src/summarization/` or `src/web/`
- ❌ Change the `QuizQuestion` or `QuizOutput` dataclass structures
- ❌ Change the method signature of `generate()`
- ❌ Modify files outside your module without team discussion
- ❌ Call the Summarizer directly (web app handles that)

## Integration Points
- Your `QuizOutput` is consumed by `src/web/app.py`
- The `WebApp.process_text()` method will call your `QuizGenerator.generate()` method
- Make sure your output matches the defined `QuizQuestion` and `QuizOutput` structures exactly

## Testing
Write your tests in `tests/test_quiz.py`

Test your implementation with:
```bash
pytest tests/test_quiz.py
```

## Dependencies
If you need to add a new package:
1. Create an issue describing why
2. Get team approval
3. Update `requirements.txt`
4. Everyone installs: `pip install -r requirements.txt`

## Questions?
Check `src/quiz/models.py` to see the exact structure of `QuizQuestion` and `QuizOutput`.
