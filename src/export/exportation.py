import os
from datetime import datetime
#from .anki_exporter import AnkiExporter
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
            return self._export_to_pdf(summary, quiz)
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

        # Create PDF instance with better styling
        pdf = FPDF()
        pdf.add_page()
        
        # Define colors
        pdf.set_text_color(70, 70, 70)  # Dark gray
        pdf.set_draw_color(0, 122, 204)  # Blue
        

        # Add header with title
        pdf.set_fill_color(0, 122, 204)  # Blue background
        pdf.set_text_color(255, 255, 255)  # White text
        pdf.set_font('Arial', 'B', 24)
        pdf.cell(0, 15, 'AI Summary & Quiz Export', 0, 1, 'C', True)
        pdf.ln(5)
        
        # Add timestamp
        pdf.set_text_color(70, 70, 70)
        pdf.set_font('Arial', 'I', 10)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pdf.cell(0, 6, f'Generated on: {timestamp}', 0, 1, 'C')
        pdf.ln(10)
        
        # Add decorative line
        pdf.set_line_width(0.5)
        pdf.line(20, pdf.get_y(), 190, pdf.get_y())
        pdf.ln(5)
        
        # Export summary if provided
        if summary:

            # Summary section header
            pdf.set_fill_color(248, 250, 252)  # Light blue background
            pdf.set_text_color(0, 122, 204)  # Blue text
            pdf.set_font('Arial', 'B', 18)
            pdf.cell(0, 12, 'SUMMARY', 0, 1, 'L', True)
            pdf.ln(5)
            

            # Summary text box
            pdf.set_fill_color(248, 249, 250)
            pdf.set_text_color(70, 70, 70)
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 8, 'Summary:', 0, 1, 'L', True)
            pdf.ln(1)
            
            pdf.set_font('Arial', '', 11)
            summary_text = summary.summary if isinstance(summary.summary, str) else ' '.join(summary.summary)
            pdf.multi_cell(0, 6, summary_text, 1, 'L', True)
            pdf.ln(5)
            

            if summary.title:
                pdf.set_fill_color(238, 141, 189)  # Light pink
                pdf.set_text_color(185, 20, 185)  # Dark pink
                pdf.set_font('Arial', 'B', 14)
                pdf.cell(0, 10, 'Title', 0, 1, 'C', True)
                pdf.ln(2)

                pdf.set_fill_color(255, 255, 255)
                pdf.set_text_color(70, 70, 70)
                pdf.set_font('Arial', '', 11)
                if isinstance(summary.title, list):
                    title_text = summary.title[0]
                else:
                    title_text = summary.title
                pdf.multi_cell(0, 6, title_text, 1, 'L', True)
                pdf.ln(5)
            
            # Bullet points
            if summary.bullet_points:
                pdf.set_fill_color(232, 244, 248)  # Light blue
                pdf.set_text_color(0, 122, 204)
                pdf.set_font('Arial', 'B', 14)
                pdf.cell(0, 10, 'Key Points', 0, 1, 'C', True)
                pdf.ln(2)
                
                pdf.set_fill_color(255, 255, 255)
                pdf.set_text_color(70, 70, 70)

                pdf.set_font('Arial', '', 11)
                for i, point in enumerate(summary.bullet_points, 1):
                    pdf.multi_cell(0, 6, f'- {point}', 1, 'L', True)
                    if i < len(summary.bullet_points):
                        pdf.ln(1)
                pdf.ln(5)
            

            # Key concepts
            if summary.key_concepts:
                pdf.set_fill_color(255, 243, 205)  # Light yellow
                pdf.set_text_color(133, 77, 0)  # Dark yellow
                pdf.set_font('Arial', 'B', 14)
                pdf.cell(0, 10, 'Key Concepts', 0, 1, 'C', True)
                pdf.ln(2)
                

                pdf.set_fill_color(255, 255, 255)
                pdf.set_text_color(70, 70, 70)
                pdf.set_font('Arial', '', 11)
                concepts_text = ' - '.join([f'"{concept}"' for concept in summary.key_concepts])
                pdf.multi_cell(0, 6, concepts_text, 1, 'L', True)
                pdf.ln(5)
            

            if summary.source:
                pdf.set_fill_color(180, 141, 239)  # Light purple
                pdf.set_text_color(61,22, 118) # Dark purple
                pdf.set_font('Arial', 'B', 14)
                pdf.cell(0, 10, 'Source', 0, 1, 'C', True)
                pdf.ln(2)

                pdf.set_fill_color(255, 255, 255)
                pdf.set_text_color(70, 70, 70)
                pdf.set_font('Arial', '', 11)
                
                # Handle both string and list sources
                if isinstance(summary.source, list):
                    source_text = '\n'.join(summary.source)
                else:
                    source_text = str(summary.source)
                pdf.multi_cell(0, 6, source_text, 1, 'L', True)
                pdf.ln(5)

            # Metadata box
            pdf.set_fill_color(241, 243, 244)  # Light gray
            pdf.set_text_color(102, 102, 102)

            pdf.set_font('Arial', 'I', 9)
            pdf.multi_cell(0, 5, f'Metadata:\n* Text Length: {summary.text_length:,} characters\n* Processing Time: {summary.processing_time:.2f} seconds', 1, 'L', True)
            pdf.ln(10)
        
        # Add separator if we have both summary and quiz
        if summary and quiz:
            pdf.set_line_width(1)
            pdf.set_draw_color(0, 122, 204)
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(5)
        

        # Export quiz if provided
        if quiz:
            # Quiz section header
            pdf.set_fill_color(0, 122, 204)  # Blue background
            pdf.set_text_color(255, 255, 255)  # White text
            pdf.set_font('Arial', 'B', 18)
            pdf.cell(0, 12, 'QUIZ', 0, 1, 'L', True)
            pdf.ln(5)
            
            # Quiz stats
            pdf.set_fill_color(233, 236, 239)
            pdf.set_text_color(70, 70, 70)
            pdf.set_font('Arial', '', 11)
            pdf.cell(0, 8, f'Total Questions: {quiz.total_questions}', 0, 1, 'L', True)
            pdf.cell(0, 8, f'Source Text Length: {len(quiz.source_text):,} characters', 0, 1, 'L', True)
            pdf.ln(5)
            

            # Quiz questions
            for i, question in enumerate(quiz.questions, 1):
                                
                # Difficulty badge
                if question.difficulty == 'easy':
                    pdf.set_fill_color(189, 243, 142)  # Light lime
                    pdf.set_text_color(21, 87, 36)  # Dark green
                elif question.difficulty == 'medium':
                    pdf.set_fill_color(245, 200, 110)  # Light orange
                    pdf.set_text_color(153, 51, 0)  # Dark orange
                else:  # hard
                    pdf.set_fill_color(248, 215, 218)  # Light red
                    pdf.set_text_color(114, 28, 36)  # Dark red
                
                pdf.set_font('Arial', 'I', 9)
                pdf.cell(0, 6, f'Difficulty: {question.difficulty.upper()}', 0, 1, 'L', True)
                pdf.ln(3)
                
                # Question header
                pdf.set_fill_color(255, 255, 255)
                pdf.set_text_color(0, 122, 204)  # Blue
                pdf.set_font('Arial', 'B', 12)
                pdf.cell(0, 10, f'Question {i}:', 0, 1, 'L', True)
                
                pdf.set_fill_color(255, 255, 255)
                pdf.set_text_color(70, 70, 70)
                pdf.set_font('Arial', '', 11)
                pdf.multi_cell(0, 6, question.question, 1, 'L', True)
                pdf.ln(3)
                
                # Options
                pdf.set_fill_color(248, 249, 250)
                pdf.set_text_color(70, 70, 70)
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(0, 6, 'Options:', 0, 1, 'L', True)
                pdf.ln(1)
                
                pdf.set_font('Arial', '', 10)
                for j, option in enumerate(question.options, 1):
                    option_label = chr(64 + j)  # A, B, C, D
                    pdf.set_fill_color(255, 255, 255)
                    pdf.cell(0, 5, f'  {option_label}) {option}', 0, 1, 'L', True)
                
                pdf.ln(3)
                
                # Answer
                pdf.set_fill_color(212, 237, 218)
                pdf.set_text_color(21, 87, 36)
                pdf.set_font('Arial', 'B', 11)
                pdf.cell(0, 7, f'Answer: {question.answer}', 0, 1, 'L', True)
                pdf.ln(5)

        
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
                "title": summary.title,
                "summary": summary.summary,
                "bullet_points": summary.bullet_points,
                "key_concepts": summary.key_concepts,
                "source": summary.source,
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
    


    def _export_to_html(self, summary: SummaryOutput = None, quiz: QuizOutput = None, hide_answers: bool = False) -> str:
        """Export results to HTML format."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # JavaScript for answer toggle
        toggle_script = """
    <script>
        function toggleAnswers() {
            const answers = document.querySelectorAll('.answer');
            const button = document.getElementById('toggleBtn');
            const hidden = answers[0].style.display === 'none';
            
            answers.forEach(answer => {
                answer.style.display = hidden ? 'block' : 'none';
            });
            
            button.textContent = hidden ? '🔒 Hide Answers' : '👁️ Show Answers';
        }
        
        function initializeAnswers() {
            const answers = document.querySelectorAll('.answer');
            if (""" + str(hide_answers).lower() + """) {
                answers.forEach(answer => answer.style.display = 'none');
                document.getElementById('toggleBtn').textContent = '👁️ Show Answers';
            }
        }
        
        window.addEventListener('load', initializeAnswers);
    </script>
"""
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Summary & Quiz Export</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        

        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .header {{
            background-color: #007acc;
            color: white;
            padding: 30px;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 30px;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            font-weight: bold;
            margin: 0;
        }}
        
        .timestamp {{
            margin-top: 10px;
            font-size: 1rem;
            opacity: 0.9;
        }}
        
        .main-content {{
            padding: 0;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section-title {{
            font-size: 1.8rem;
            color: #333;
            border-bottom: 2px solid #007acc;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        
        .summary-text {{
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(79, 70, 229, 0.1);
            margin: 25px 0;
            font-size: 1.1rem;
            line-height: 1.8;
            box-shadow: 
                0 4px 6px rgba(0, 0, 0, 0.05),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }}
        
        .summary-title {{
            background: linear-gradient(135deg, #fdf2f8 0%, #fce7f3 100%);
            padding: 25px;
            border-radius: 16px;
            margin: 20px 0;
            border: 1px solid rgba(236, 72, 153, 0.1);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }}
        
        .summary-title h3 {{
            background: linear-gradient(135deg, #ec4899, #be185d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
            margin-bottom: 10px;
        }}
        
        .bullet-points {{
            background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
            padding: 30px;
            border-radius: 20px;
            margin: 25px 0;
            border: 1px solid rgba(34, 197, 94, 0.1);
        }}
        
        .bullet-points h3 {{
            color: #059669;
            font-weight: 600;
            margin-bottom: 20px;
        }}
        
        .bullet-points ul {{
            list-style: none;
            padding: 0;
        }}
        
        .bullet-points li {{
            margin-bottom: 12px;
            font-weight: 500;
            position: relative;
            padding-left: 30px;
        }}
        
        .bullet-points li::before {{
            content: '✓';
            position: absolute;
            left: 0;
            color: #059669;
            font-weight: bold;
            font-size: 1.1rem;
        }}
        
        .key-concepts {{
            background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
            padding: 25px;
            border-radius: 16px;
            margin: 20px 0;
            border: 1px solid rgba(245, 158, 11, 0.1);
        }}
        
        .key-concepts h3 {{
            color: #d97706;
            font-weight: 600;
            margin-bottom: 15px;
        }}
        
        .concept-tag {{
            display: inline-block;
            background: linear-gradient(135deg, #f59e0b, #d97706);
            color: white;
            padding: 8px 16px;
            margin: 4px 6px 4px 0;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: 500;
            box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);
            transition: transform 0.2s ease;
        }}
        
        .concept-tag:hover {{
            transform: translateY(-1px);
        }}
        
        .sources {{
            background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%);
            padding: 25px;
            border-radius: 16px;
            margin: 20px 0;
            border: 1px solid rgba(168, 85, 247, 0.1);
        }}
        
        .sources h3 {{
            background: linear-gradient(135deg, #8b5cf6, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
            margin-bottom: 15px;
        }}
        
        .sources ul {{
            list-style: none;
            padding: 0;
        }}
        
        .sources li {{
            margin-bottom: 8px;
            position: relative;
            padding-left: 25px;
            font-weight: 500;
        }}
        
        .sources li::before {{
            content: '📚';
            position: absolute;
            left: 0;
            font-size: 0.9rem;
        }}
        
        .metadata {{
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            padding: 20px;
            border-radius: 12px;
            font-size: 0.9rem;
            color: #64748b;
            border: 1px solid #e2e8f0;
            font-family: 'JetBrains Mono', monospace;
        }}
        
        .quiz-controls {{
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            border-radius: 16px;
            border: 1px solid #cbd5e1;
        }}
        
        .toggle-btn {{
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(79, 70, 229, 0.3);
        }}
        
        .toggle-btn:hover {{
            transform: translateY(-1px);
            box-shadow: 0 6px 12px rgba(79, 70, 229, 0.4);
        }}
        
        .quiz-question {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 
                0 4px 6px rgba(0, 0, 0, 0.05),
                0 1px 3px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        
        .quiz-question:hover {{
            transform: translateY(-2px);
            box-shadow: 
                0 8px 25px rgba(0, 0, 0, 0.1),
                0 4px 6px rgba(0, 0, 0, 0.05);
        }}
        
        .question-title {{
            color: #1e293b;
            font-size: 1.4rem;
            font-weight: 600;
            margin-bottom: 20px;
            line-height: 1.4;
        }}
        
        .options {{
            margin: 20px 0;
        }}
        
        .option {{
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            padding: 15px 20px;
            margin: 10px 0;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            transition: all 0.2s ease;
            position: relative;
        }}
        
        .option:hover {{
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            border-color: #4f46e5;
            transform: translateX(5px);
        }}
        
        .option-label {{
            font-weight: 700;
            color: #4f46e5;
            margin-right: 10px;
        }}
        
        .answer {{
            background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
            color: #166534;
            padding: 15px 20px;
            border-radius: 12px;
            margin: 15px 0;
            border: 1px solid rgba(34, 197, 94, 0.2);
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        
        .difficulty {{
            display: inline-block;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .difficulty.easy {{
            background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
            color: #166534;
        }}
        
        .difficulty.medium {{
            background: linear-gradient(135deg, #fef3c7 0%, #fed7aa 100%);
            color: #92400e;
        }}
        
        .difficulty.hard {{
            background: linear-gradient(135deg, #fecaca 0%, #fbb6ce 100%);
            color: #991b1b;
        }}
        
        .quiz-stats {{
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            padding: 25px;
            border-radius: 16px;
            margin-bottom: 30px;
            text-align: center;
            border: 1px solid #cbd5e1;
        }}
        
        .stat-item {{
            display: inline-block;
            margin: 0 25px;
            font-weight: 600;
            color: #475569;
            font-size: 1.1rem;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                margin: 10px;
                border-radius: 16px;
            }}
            
            .header {{
                padding: 30px 20px;
            }}
            
            .header h1 {{
                font-size: 2.2rem;
            }}
            
            .main-content {{
                padding: 30px 20px;
            }}
            
            .stat-item {{
                display: block;
                margin: 10px 0;
            }}
        }}
    </style>
    """ + toggle_script + """
</head>
<body>
    <div class="container">

        <div class="header">
            <h1>📄 AI Summary & Quiz Export</h1>
            <div class="timestamp">Generated on: {timestamp}</div>
        </div>
        <div class="main-content">"""
        
        # Add summary section if provided
        if summary:
            html_content += f"""
            <div class="section">
                <h2 class="section-title">📝 Summary</h2>
                
                <div class="summary-text">
                    <strong>Summary:</strong><br>
                    {summary.summary}
                </div>"""
            
            # Add title section if provided
            if summary.title:
                html_content += f"""
                <div class="summary-title">
                    <h3>📋 Title:</h3>
                    <p style="font-weight: 500; color: #1e293b; margin: 0;">{summary.title[0] if isinstance(summary.title, list) else summary.title}</p>
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
                
                # Add sources section if provided
                if summary.source:
                    html_content += f"""
                <div class="sources">
                    <h3>📚 Sources:</h3>
                    <ul>"""
                    for source in (summary.source if isinstance(summary.source, list) else [summary.source]):
                        html_content += f"<li>{source}</li>"
                    html_content += """
                    </ul>
                </div>"""
                
                html_content += f"""
                <div class="metadata">
                    <strong>Metadata:</strong><br>
                    Text Length: {summary.text_length:,} characters<br>
                    Processing Time: {summary.processing_time:.2f} seconds
                </div>
            </div>"""
        
        # Add quiz section if provided
        if quiz:
            html_content += f"""
            <div class="section">
                <h2 class="section-title">❓ Quiz</h2>
                
                <div class="quiz-controls">
                    <button id="toggleBtn" class="toggle-btn" onclick="toggleAnswers()">🔒 Hide Answers</button>
                </div>
                
                <div class="quiz-stats">
                    <div class="stat-item">📊 Total Questions: {quiz.total_questions}</div>
                    <div class="stat-item">📝 Source Length: {len(quiz.source_text):,} chars</div>
                </div>"""
            
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
                        <strong>✓ Answer:</strong> {question.answer}
                    </div>
                    
                    <div class="difficulty {question.difficulty}">
                        {question.difficulty}
                    </div>
                </div>"""
            
            html_content += """
            </div>"""
        
        html_content += """
        </div>
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

"""
            
            # Add title if provided
            if summary.title:
                title_text = summary.title[0] if isinstance(summary.title, list) else summary.title
                markdown_content += f"### Title\n{title_text}\n\n"
            
            markdown_content += "### Summary\n"
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
            
            # Add sources if provided
            if summary.source:
                markdown_content += "### Sources\n"
                if isinstance(summary.source, list):
                    for source in summary.source:
                        markdown_content += f"- {source}\n"
                else:
                    markdown_content += f"- {summary.source}\n"
                markdown_content += "\n"
            
            markdown_content += "### Metadata\n"
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

    """def _export_to_anki(self, quiz: QuizOutput) -> str:
        #Export quiz results to Anki .apkg format.
        anki_exporter = AnkiExporter()
        apkg_path = anki_exporter.create_apkg(quiz)
        return apkg_path"""
