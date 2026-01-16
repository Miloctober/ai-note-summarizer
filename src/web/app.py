import sys
import os

from src.summarization.summarizer import Summarizer
from src.quiz.generator import QuizGenerator
from src.export.exportation import Exportation
from PyPDF2 import PdfReader

from pathlib import Path
from flask import Flask, render_template, request, send_file

sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)


class WebApp:
    def __init__(self):
        self.summarizer = Summarizer()
        self.quiz_generator = QuizGenerator()
        self.exporter = Exportation()

    def process_text(self, text: str):
        if not text or not text.strip():
            raise ValueError("Text given is empty.")
        text = text.strip()
        if len(text) < 100:
            raise ValueError("Text given is too short.")
        summary = self.summarizer.summarize(text)
        quiz = self.quiz_generator.generate(text)
        return {"summary": summary, "quiz": quiz}


webapp = WebApp()



@app.route("/", methods=["GET"])
def index():
    return render_template("attempt.html")


def extract_text_from_pdf():
    pdf = request.files.get("pdf")

    if not pdf or pdf.filename == "":
        return "None"
    else:
        reader = PdfReader(pdf.stream)
        return "\n".join(page.extract_text() or "" for page in reader.pages)



@app.post("/run")
def run():
    text = request.form.get("text", "").strip()
    action = request.form.get("action", "")  # summary|quiz|both

    t_pdf = extract_text_from_pdf()
 
    if len(t_pdf) >= 100:
        text += t_pdf
        
    if not text:
        return render_template("attempt.html", error="Please paste some text first.", text="")

        
    # length constraint
    if len(text) < 100:
        return render_template("attempt.html", error="Text given is too short (min 100 chars).", text=text)

    try:
        ctx = {"text": text}

        if action in ("summary", "both"):
            out = webapp.summarizer.summarize(text) 
            sources = out.source.pop(0)
            ctx.update({
                "title": (out.title[0] if isinstance(out.title, list) and out.title else out.title),
                "summary": out.title[2],
                "bullet_points": out.bullet_points,
                "key_concepts": out.key_concepts,
                "sources": out.source,
            })

        if action in ("quiz", "both"):
            qout = webapp.quiz_generator.generate(text)
            # pass list of questions to Jinja
            ctx["quiz"] = qout.questions

        return render_template("attempt.html", **ctx)

    except ValueError as e:
        return render_template("attempt.html", error=str(e), text=text)


@app.post("/export")
def export():
    text = request.form.get("text", "").strip()
    export_format = request.form.get("format", "pdf")   # pdf|json|html|markdown|anki
    export_what = request.form.get("export_what", "both")  # summary|quiz|both

    if not text:
        return render_template("attempt.html", error="Please paste some text first.", text="")

    if len(text) < 100:
        return render_template("attempt.html", error="Text given is too short (min 100 chars).", text=text)

    # Compute only what you plan to export
    summary_out = None
    quiz_out = None

    if export_what in ("summary", "both"):
        summary_out = webapp.summarizer.summarize(text)

    if export_what in ("quiz", "both"):
        quiz_out = webapp.quiz_generator.generate(text)


    try:
        file_path = webapp.exporter.export_results(export_format, summary=summary_out, quiz=quiz_out)
        path = Path(file_path).resolve()
        if not path.exists():
            return render_template("attempt.html", error=f"Export failed: file not found at {path}", text=text)

        return send_file(path, as_attachment=True, download_name=path.name)

    except ValueError as e:
        return render_template("attempt.html", error=str(e), text=text)





if __name__ == "__main__":
    app.run(debug=True)