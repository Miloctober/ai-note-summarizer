from .models import SummaryOutput


class Summarizer:
    """Generates summaries from input text."""
    
    def summarize(self, text: str) -> SummaryOutput:
        """
        Generate a summary from input text.
        
        Args:
            text: Raw lecture notes or document text
            
        Returns:
            SummaryOutput with summary, bullets, and concepts
            
        Raises:
            ValueError: If text is empty or too short
        """
        pass
