from .models import QuizOutput, QuizQuestion


class QuizGenerator:
    """Generates quiz questions from input text."""
    
    def generate(self, text: str) -> QuizOutput:
        """
        Generate quiz questions from input text.
        
        Args:
            text: Raw lecture notes or document text to generate questions from
            
        Returns:
            QuizOutput with generated questions and metadata
            
        Raises:
            ValueError: If text is empty or too short
        """
        pass
