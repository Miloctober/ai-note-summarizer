from src.summarization import Summarizer, SummaryOutput
from src.quiz import QuizGenerator, QuizOutput


class WebApp:
    """Web application interface for text summarization and quiz generation."""
    
    def __init__(self):
        """Initialize the web app with summarizer and quiz generator."""
        self.summarizer = Summarizer()
        self.quiz_generator = QuizGenerator()
    
    def process_text(self, text: str) -> dict:
        """
        Process input text through summarization and quiz generation.
        
        Args:
            text: User input text to process
            
        Returns:
            Dictionary with 'summary' (SummaryOutput) and 'quiz' (QuizOutput) keys
            
        Raises:
            ValueError: If text is empty or too short
        """
        pass
    
