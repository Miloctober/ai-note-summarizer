#!/usr/bin/env python3
"""Test script for export functionality."""

import sys
import os
sys.path.append('/Users/milothegod/ai-note-summarizer')

from src.summarization.models import SummaryOutput
from src.quiz.models import QuizOutput, QuizQuestion
from src.export.exportation import Exportation

def create_test_data():
    """Create sample test data."""
    # Create sample summary
    summary = SummaryOutput(
        summary="This is a test summary about machine learning and artificial intelligence.",
        bullet_points=[
            "Machine learning is a subset of AI",
            "Deep learning uses neural networks",
            "Supervised learning requires labeled data"
        ],
        key_concepts=["AI", "ML", "Neural Networks", "Training Data"],
        text_length=150,
        processing_time=2.5
    )
    
    # Create sample quiz
    questions = [
        QuizQuestion(
            question="What is machine learning?",
            answer="A subset of AI that enables computers to learn",
            options=["A programming language", "A subset of AI that enables computers to learn", "A database system", "A web framework"],
            difficulty="medium"
        ),
        QuizQuestion(
            question="Which technique uses neural networks?",
            answer="Deep learning",
            options=["Machine learning", "Deep learning", "Data mining", "Statistical analysis"],
            difficulty="hard"
        )
    ]
    
    quiz = QuizOutput(
        questions=questions,
        total_questions=2,
        source_text="Sample text about machine learning and AI techniques."
    )
    
    return summary, quiz


def test_exports():
    """Test all export formats."""
    print("🧪 Testing Export Functionality")
    print("=" * 50)
    
    # Create test data
    summary, quiz = create_test_data()
    
    # Initialize exporter
    exporter = Exportation()
    
    # Ensure we're running from the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir('/Users/milothegod/ai-note-summarizer')
    
    # Test formats
    formats = ["json", "markdown", "html", "pdf", "anki"]
    
    for format_name in formats:
        try:
            print(f"\n📤 Testing {format_name.upper()} export...")
            
            # Export based on format
            if format_name == "anki":
                # Anki only works with quiz data
                filepath = exporter.export_results(format=format_name, quiz=quiz)
            elif format_name == "pdf":
                # Test both summary and quiz in PDF
                print("   📝 Testing PDF with summary...")
                filepath1 = exporter.export_results(format=format_name, summary=summary)
                print("   📝 Testing PDF with quiz...")
                filepath2 = exporter.export_results(format=format_name, quiz=quiz)
                filepath = f"{filepath1} and {filepath2}"
            else:
                # Other formats can take both summary and quiz
                filepath = exporter.export_results(format=format_name, summary=summary, quiz=quiz)
            
            print(f"✅ {format_name.upper()} export successful!")
            print(f"   📁 File saved at: {filepath}")
            
            # Show file size(s)
            if " and " in str(filepath):
                files = str(filepath).split(" and ")
                for file in files:
                    if os.path.exists(file):
                        size = os.path.getsize(file)
                        print(f"   📊 File size: {size} bytes - {file}")
            else:
                if os.path.exists(filepath):
                    size = os.path.getsize(filepath)
                    print(f"   📊 File size: {size} bytes")
            
        except Exception as e:
            print(f"❌ {format_name.upper()} export failed: {str(e)}")
            import traceback
            traceback.print_exc()
    
    print(f"\n🎉 Export testing completed!")
    print(f"📂 Check the exports/ directory for generated files.")
    
    # List all generated files
    print(f"\n📋 Generated files:")
    exports_dir = "exports"
    if os.path.exists(exports_dir):
        for file in os.listdir(exports_dir):
            filepath = os.path.join(exports_dir, file)
            size = os.path.getsize(filepath)
            print(f"   📄 {file} ({size} bytes)")

if __name__ == "__main__":
    test_exports()
