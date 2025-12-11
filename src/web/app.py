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
    
    def export_results(self, summary: SummaryOutput, quiz: QuizOutput, format: str) -> str:
        """
        Export results in the specified format.
        
        Args:
            summary: SummaryOutput object to export
            quiz: QuizOutput object to export
            format: Export format ("pdf", "json", "html", etc.)
            
        Returns:
            Path to exported file or file content as string
            
        Raises:
            ValueError: If format is not supported
        """
        pass
