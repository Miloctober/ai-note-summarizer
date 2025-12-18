from ai_summarizer.summarization.summarizer import Summarizer, SummaryOutput
from ai_summarizer.quiz.generator import QuizGenerator, QuizOutput


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
        # Milo: N'oublie pas de faire d'appeller ma fonction pour l'exportation! 
        # Tu dois t'assurer que dans la fonction export_results tu précises bien le format et si c'est un quiz 
        # ou un résumé :) Bon courage !
        pass
    
