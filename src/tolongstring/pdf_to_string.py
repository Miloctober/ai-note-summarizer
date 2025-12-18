from pypdf import PdfReader
import io

def pdf_bytes_to_text_string(pdf_bytes: bytes) -> str:
    reader = PdfReader(io.BytesIO(pdf_bytes))
    parts = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        text = " ".join(text.split())
        if text:
            parts.append(f"[PAGE {i+1}] {text}")
    return str("\n".join(parts).strip())
