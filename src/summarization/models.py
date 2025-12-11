from dataclasses import dataclass


@dataclass
class SummaryOutput:
    """Output structure for summarization results."""
    summary: str           # Main summary paragraph
    bullet_points: list    # List of key points
    key_concepts: list     # List of terms/concepts
    text_length: int       # Original text length
    processing_time: float # How long it took
