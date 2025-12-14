"""
Anki Flashcards Export Module
Creates .apkg files compatible with Anki for quiz-based flashcards.
"""
import json
import sqlite3
import zipfile
import tempfile
import os
from datetime import datetime
from typing import List, Dict
from src.quiz.models import QuizOutput, QuizQuestion

class AnkiExporter:
    """Exports QuizOutput to Anki .apkg format."""
    
    def __init__(self):
        """Initialize Anki exporter."""
        self.model_id = "1695219123361"  # Basic model ID
        self.deck_id = "1695219123361"   # Basic deck ID
    
    