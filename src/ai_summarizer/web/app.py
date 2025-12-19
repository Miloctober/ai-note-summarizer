from ai_summarizer.summarization.summarizer import Summarizer, SummaryOutput
from ai_summarizer.quiz.generator import QuizGenerator, QuizOutput
from ai_summarizer.export.exportation import Exportation
from ai_summarizer.export.anki_exporter import AnkiExporter

from pathlib import Path

from flask import Flask, render_template, redirect, request, send_file


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
        if not text or not text.strip():
            raise ValueError("Text given is empty.")

        text = text.strip()
        if len(text) < 100:
            raise ValueError("Text given is too short.")

        summary = self.summarizer.summarize(text)
        quiz = self.quiz_generator.generate(text)

        process = {"summary": summary,"quiz": quiz}

        return process



app = Flask(__name__)
webapp = WebApp()

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/summary")
def do_summary():
    text = request.form.get("text", "").strip()
    if len(text) < 1:
        return render_template("index.html", error="Please paste some text first.")
    # TODO: replace with: summary = webapp.summarizer.summarize(text)
    out = webapp.summarizer.summarize(text)
    return render_template("index.html",text=text,title=(out.title[0] if isinstance(out.title, list) and out.title else out.title),
    summary= out.summary,   # nice clean paragraph
    bullet_points=out.bullet_points,
    key_concepts=out.key_concepts,
    sources=out.source,
)

@app.post("/quiz")
def do_quiz():
    text = request.form.get("text", "").strip()
    if len(text) < 1:
        return render_template("index.html", error="Please paste some text first.")
    # TODO: replace with: quiz = webapp.quiz_generator.generate(text)
    quiz = webapp.quiz_generator.generate(text)
    return render_template("index.html", text=text, quiz= quiz.questions )

@app.post("/export")
def do_export():
    text = request.form.get("text", "").strip()
    if len(text) < 1:
        return render_template("index.html", error="Please paste some text first.")

    export_format = request.form.get("format", "pdf")

    summary_out = webapp.summarizer.summarize(text)
    quiz_out = webapp.quiz_generator.generate(text)

    exporter = Exportation()
    file_path = exporter.export_results(export_format, summary=summary_out, quiz=quiz_out)

    path = Path(file_path).resolve()
    if not path.exists():
        return render_template("index.html", error="Export failed.", text=text)

    return send_file(path, as_attachment=True, download_name=path.name)


if __name__ == "__main__":
    app.run(debug=True)
  

    
