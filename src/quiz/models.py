from dataclasses import dataclass
from typing import List

MODEL_NAME = "gpt-oss:20b-cloud"

@dataclass
class QuizQuestion:
    """Represents a single quiz question."""
    question: str
    answer: str
    options: List[str]  # 4 multiple choice options
    difficulty: str     # "easy", "medium", "hard"


@dataclass
class QuizOutput:
    """Output structure for quiz generation results."""
    questions: List[QuizQuestion]
    total_questions: int
    source_text: str
