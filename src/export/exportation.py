import os
from datetime import datetime
from src.export.anki_exporter import AnkiExporter
from src.summarization import Summarizer, SummaryOutput
from src.quiz import QuizGenerator, QuizOutput
from fpdf import FPDF

class Exportation:
    """Class responsible for exporting summary and quiz results."""
    def __init__(self):
        """Initialize the exportation class."""
        pass
    

    def export_results(self, format: str, summary: SummaryOutput = None, quiz: QuizOutput = None) -> str:
        """
        Export results in the specified format.
        
        Args:
            summary: SummaryOutput object to export
            quiz: QuizOutput object to export
            format: Export format ("pdf", "json", "html", etc.)

        Format organisation:
        - PDF: Pretty formatted document for summaries and/or quizzes.
        - JSON: Structured data for summaries and/or quizzes.
        - HTML: Web-friendly format for summaries and/or quizzes.
        - Markdown: Markdown formatted text for summaries and/or quizzes.
        - Anki: .apkg file for quiz flashcards (Question/Answer).
                
        Returns:
            Path to exported file or file content as string
                
        Raises:
            ValueError: If format is not supported
        """
        if format == "anki":
            return self._export_to_anki(quiz)
        elif format == "pdf":
            return self._export_to_pdf(summary)
        elif format == "json":
            return self._export_to_json(summary, quiz)
        elif format == "html":
            return self._export_to_html(summary, quiz)
        elif format == "markdown":
            return self._export_to_markdown(summary, quiz)
        else:
            raise ValueError(f"Unsupported export format: {format}")



    def _export_to_pdf(self, summary: SummaryOutput = None, quiz: QuizOutput = None) -> str:
        """Export results to PDF format."""
        
        # Check if we have any content to export
        if not summary and not quiz:
            raise ValueError("At least one of summary or quiz must be provided for PDF export")

        # Create PDF instance
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        

        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pdf.cell(0, 10, f'Generated on: {timestamp}', 0, 1)
        pdf.ln(10)
        
        # Export summary if provided
        if summary:
            pdf.set_font('Arial', 'B', 18)
            pdf.cell(0, 10, 'SUMMARY', 0, 1)
            pdf.ln(5)
            
            # Summary text
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 8, f'Summary: {summary.summary}')
            pdf.ln(5)
            
            # Bullet points
            if summary.bullet_points:
                pdf.set_font('Arial', 'B', 14)
                pdf.cell(0, 10, 'Key Points:', 0, 1)
                pdf.set_font('Arial', '', 12)
                for i, point in enumerate(summary.bullet_points, 1):
                    pdf.cell(0, 6, f'{i}. {point}', 0, 1)
                pdf.ln(5)
            
            # Key concepts
            if summary.key_concepts:
                pdf.set_font('Arial', 'B', 14)
                pdf.cell(0, 10, 'Key Concepts:', 0, 1)
                pdf.set_font('Arial', '', 12)
                concepts_text = ', '.join(summary.key_concepts)
                pdf.multi_cell(0, 6, concepts_text)
                pdf.ln(5)
            
            # Metadata
            pdf.set_font('Arial', 'I', 10)
            pdf.cell(0, 6, f'Text Length: {summary.text_length} characters', 0, 1)
            pdf.cell(0, 6, f'Processing Time: {summary.processing_time:.2f} seconds', 0, 1)
            pdf.ln(10)
        
        # Add separator if we have both summary and quiz
        if summary and quiz:
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, '═══════════════════════════════════════════', 0, 1)
            pdf.ln(5)
        
        # Export quiz if provided
        if quiz:
            pdf.set_font('Arial', 'B', 18)
            pdf.cell(0, 10, 'QUIZ', 0, 1)
            pdf.ln(5)
            
            pdf.set_font('Arial', '', 12)
            pdf.cell(0, 6, f'Total Questions: {quiz.total_questions}', 0, 1)
            pdf.cell(0, 6, f'Source Text Length: {len(quiz.source_text)} characters', 0, 1)
            pdf.ln(5)
            
            # Quiz questions
            for i, question in enumerate(quiz.questions, 1):
                pdf.set_font('Arial', 'B', 14)
                pdf.multi_cell(0, 8, f'Question {i}: {question.question}')
                pdf.set_font('Arial', '', 12)
                pdf.cell(0, 6, 'Options:', 0, 1)
                
                for j, option in enumerate(question.options, 1):
                    pdf.cell(0, 6, f'  {chr(64+j)}) {option}', 0, 1)
                
                pdf.set_font('Arial', 'B', 12)
                pdf.cell(0, 6, f'Answer: {question.answer}', 0, 1)
                pdf.cell(0, 6, f'Difficulty: {question.difficulty.title()}', 0, 1)
                pdf.ln(8)
        
        # If no content was added (both summary and quiz are None)
        if not summary and not quiz:
            pdf.set_font('Arial', '', 12)
            pdf.cell(0, 10, 'No content to export', 0, 1)

        # Save PDF
        os.makedirs("exports", exist_ok=True)
        filename = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = f"exports/{filename}"
        
        pdf.output(filepath)
        return filepath


    def _export_to_json(self, summary: SummaryOutput = None, quiz: QuizOutput = None) -> str:
        """Export results to JSON format."""
        import json
        
        # Create export data structure
        export_data = {
            "timestamp": datetime.now().isoformat(),
            "export_info": {
                "generated_by": "AI Note Summarizer",
                "version": "1.0"
            }
        }
        
        # Add summary data if provided
        if summary:
            export_data["summary"] = {
                "summary": summary.summary,
                "bullet_points": summary.bullet_points,
                "key_concepts": summary.key_concepts,
                "text_length": summary.text_length,
                "processing_time": summary.processing_time
            }
        
        # Add quiz data if provided
        if quiz:
            export_data["quiz"] = {
                "total_questions": quiz.total_questions,
                "source_text_length": len(quiz.source_text),
                "questions": []
            }
            
            for question in quiz.questions:
                export_data["quiz"]["questions"].append({
                    "question": question.question,
                    "answer": question.answer,
                    "options": question.options,
                    "difficulty": question.difficulty
                })
        

        # Save JSON file
        os.makedirs("exports", exist_ok=True)
        filename = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = f"exports/{filename}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        return filepath
    

    def _export_to_html(self, summary: SummaryOutput = None, quiz: QuizOutput = None) -> str:
        """Export results to HTML format."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Summary & Quiz Export</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            border-bottom: 3px solid #007acc;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            color: #007acc;
            margin: 0;
            font-size: 2.5em;
        }}
        .timestamp {{
            color: #666;
            font-style: italic;
            margin-top: 10px;
        }}
        .section {{
            margin-bottom: 40px;
        }}
        .section-title {{
            color: #333;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.8em;
        }}
        .summary-text {{
            background: #f8f9fa;
            padding: 20px;
            border-left: 4px solid #007acc;
            margin: 20px 0;
            font-size: 1.1em;
        }}
        .bullet-points {{
            background: #e8f4f8;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .bullet-points ul {{
            margin: 0;
            padding-left: 20px;
        }}
        .bullet-points li {{
            margin-bottom: 8px;
            font-weight: 500;
        }}
        .key-concepts {{
            background: #fff3cd;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .concept-tag {{
            display: inline-block;
            background: #ffc107;
            color: #000;
            padding: 5px 12px;
            margin: 3px;
            border-radius: 15px;
            font-size: 0.9em;
            font-weight: 500;
        }}
        .metadata {{
            background: #f1f3f4;
            padding: 15px;
            border-radius: 5px;
            font-size: 0.9em;
            color: #666;
        }}
        .quiz-question {{
            background: #ffffff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 25px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }}
        .question-title {{
            color: #007acc;
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 15px;
        }}
        .options {{
            margin: 15px 0;
        }}
        .option {{
            background: #f8f9fa;
            padding: 10px;
            margin: 8px 0;
            border-radius: 5px;
            border-left: 4px solid #007acc;
        }}
        .option-label {{
            font-weight: bold;
            color: #007acc;
        }}
        .answer {{
            background: #d4edda;
            color: #155724;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            border-left: 4px solid #28a745;
        }}
        .difficulty {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
            text-transform: uppercase;
        }}
        .difficulty.easy {{
            background: #d4edda;
            color: #155724;
        }}
        .difficulty.medium {{
            background: #fff3cd;
            color: #856404;
        }}
        .difficulty.hard {{
            background: #f8d7da;
            color: #721c24;
        }}
        .quiz-stats {{
            background: #e9ecef;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }}
        .stat-item {{
            display: inline-block;
            margin: 0 20px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📄 AI Summary & Quiz Export</h1>
            <div class="timestamp">Generated on: {timestamp}</div>"""
        
        # Add summary section if provided
        if summary:
            html_content += f"""
        <div class="section">
            <h2 class="section-title">📝 Summary</h2>
            
            <div class="summary-text">
                <strong>Summary:</strong><br>
                {summary.summary}
            </div>"""
            
            if summary.bullet_points:
                html_content += f"""
            <div class="bullet-points">
                <h3>Key Points:</h3>
                <ul>"""
                for point in summary.bullet_points:
                    html_content += f"<li>{point}</li>"
                html_content += """
                </ul>
            </div>"""
            
            if summary.key_concepts:
                html_content += f"""
            <div class="key-concepts">
                <h3>Key Concepts:</h3>"""
                for concept in summary.key_concepts:
                    html_content += f'<span class="concept-tag">{concept}</span>'
                html_content += """
            </div>"""
            
            html_content += f"""
            <div class="metadata">
                <strong>Metadata:</strong><br>
                Text Length: {summary.text_length} characters<br>
                Processing Time: {summary.processing_time:.2f} seconds
            </div>"""
        
        # Add quiz section if provided
        if quiz:
            html_content += f"""
        <div class="section">
            <h2 class="section-title">❓ Quiz</h2>
            
            <div class="quiz-stats">
                <div class="stat-item">Total Questions: {quiz.total_questions}</div>
                <div class="stat-item">Source Length: {len(quiz.source_text)} chars</div>"""
            
            for i, question in enumerate(quiz.questions, 1):
                html_content += f"""
            <div class="quiz-question">
                <div class="question-title">Question {i}: {question.question}</div>
                
                <div class="options">
                    <strong>Options:</strong><br>"""
                for j, option in enumerate(question.options):
                    option_label = chr(65 + j)  # A, B, C, D
                    html_content += f"""
                    <div class="option">
                        <span class="option-label">{option_label})</span> {option}
                    </div>"""
                
                html_content += f"""
                </div>
                
                <div class="answer">
                    <strong>Answer:</strong> {question.answer}
                </div>
                
                <div class="difficulty {question.difficulty}">
                    {question.difficulty}
                </div>"""
            
            html_content += """
        </div>"""
        
        html_content += """
    </div>
</body>
</html>"""
        

        # Save HTML file
        os.makedirs("exports", exist_ok=True)
        filename = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        filepath = f"exports/{filename}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath


    def _export_to_markdown(self, summary: SummaryOutput = None, quiz: QuizOutput = None) -> str:
        """Export results to Markdown format."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        markdown_content = f"""# 📄 AI Summary & Quiz Export

*Generated on: {timestamp}*

---

"""
        
        # Add summary section if provided
        if summary:
            markdown_content += """## 📝 Summary

### Summary
"""
            markdown_content += f"{summary.summary}\n\n"
            
            if summary.bullet_points:
                markdown_content += """### Key Points
"""
                for i, point in enumerate(summary.bullet_points, 1):
                    markdown_content += f"{i}. {point}\n"
                markdown_content += "\n"
            
            if summary.key_concepts:
                markdown_content += """### Key Concepts
"""
                for concept in summary.key_concepts:
                    markdown_content += f"`{concept}` "
                markdown_content += "\n\n"
            
            markdown_content += """### Metadata
"""
            markdown_content += f"- **Text Length:** {summary.text_length} characters\n"
            markdown_content += f"- **Processing Time:** {summary.processing_time:.2f} seconds\n\n"
            markdown_content += "---\n\n"
        
        # Add quiz section if provided
        if quiz:
            markdown_content += f"""## ❓ Quiz

### Quiz Statistics
- **Total Questions:** {quiz.total_questions}
- **Source Text Length:** {len(quiz.source_text)} characters

---

"""
            
            for i, question in enumerate(quiz.questions, 1):
                markdown_content += f"""### Question {i}: {question.question}

**Options:**
"""
                for j, option in enumerate(question.options, 1):
                    option_label = chr(64 + j)  # A, B, C, D
                    markdown_content += f"- {option_label}) {option}\n"
                
                markdown_content += f"""
**Answer:** {question.answer}

**Difficulty:** {question.difficulty.title()}

---
"""
        

        # Save markdown file
        os.makedirs("exports", exist_ok=True)
        filename = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        filepath = f"exports/{filename}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        return filepath

    def _export_to_anki(self, quiz: QuizOutput) -> str:
        """Export quiz results to Anki .apkg format.""" 
        anki_exporter = AnkiExporter()
        apkg_path = anki_exporter.create_apkg(quiz)
        return apkg_path
