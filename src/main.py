# main.py

import fitz  # PyMuPDF
import os
from docx import Document
from tqdm import tqdm

def extract_text_from_pdf(pdf_path, page_range=None):
    doc = fitz.open(pdf_path)
    text_by_page = []
    total_pages = len(doc)

    for i in tqdm(range(total_pages), desc="Estrazione pagine"):
        if page_range and i not in page_range:
            continue
        page = doc[i]
        text = page.get_text()
        text_by_page.append(text)
    doc.close()
    return text_by_page

def save_text_to_docx(texts, output_path):
    doc = Document()
    for page_num, text in enumerate(texts, 1):
        doc.add_heading(f"Pagina {page_num}", level=2)
        doc.add_paragraph(text)
        doc.add_page_break()
    doc.save(output_path)

def main():
    print("Benvenuto nel PDF Reader Tool")
    
    pdf_path = input("Inserisci il percorso del file PDF: ").strip()
    if not os.path.exists(pdf_path):
        print("❌ File non trovato. Ricontrolla il percorso.")
        return
    
    page_choice = input("Vuoi estrarre tutte le pagine? (s/n): ").strip().lower()
    if page_choice == 'n':
        pages_input = input("Inserisci i numeri di pagina separati da virgola (es. 0,1,2): ").strip()
        page_range = [int(p.strip()) for p in pages_input.split(',')]
    else:
        page_range = None

    texts = extract_text_from_pdf(pdf_path, page_range)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    file_name = os.path.basename(pdf_path).replace('.pdf', '_estratto.docx')
    output_path = os.path.join(output_dir, file_name)

    save_text_to_docx(texts, output_path)

    print(f"✅ File salvato correttamente in {output_path}")

if __name__ == "__main__":
    main()
