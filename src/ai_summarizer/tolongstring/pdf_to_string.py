from pypdf import PdfReader
import io

def pdf_bytes_to_text_string(pdf_bytes: bytes) -> str:
    '''
	convert a pdf file to a string
	
	:param pdf_bytes (bytes): bytes of a pdf file
	:return: A long string containing the extracted text of the pdf file
	:rtype: str
	'''
    reader = PdfReader(io.BytesIO(pdf_bytes))			# change the "pdf_byte" to something PdfReader can read
    parts = []											# list storing extracted text
    for i, page in enumerate(reader.pages):				# go through the pages of the PDF file
        text = page.extract_text() or ""				# extract the text, if no text, then take an empty string
        text = " ".join(text.split())					# normalize and join all the extracted text
        if text:										# append the text to the list
            parts.append(f"[PAGE {i+1}] {text}")
    return str("\n".join(parts).strip())				# join all the content of the list to a single string with a \n and normalize it by removing extra whitespace
