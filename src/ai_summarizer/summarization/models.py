from dataclasses import dataclass
# YuJin t'es super sympa t'es super fort on t'aime fort ^^
# BON COURAGE AAAAAAAH

@dataclass
class SummaryOutput:
    """Output structure for summarization results."""
    title:str              # Main title
    summary: str           # Main summary paragraph
    bullet_points: list    # List of key points
    key_concepts: list     # List of terms/concepts
    text_legnth: int       # Original text length
    processing_time: float # How long it took
    source: list           # sources of doc


