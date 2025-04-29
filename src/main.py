# src/main.py

import argparse
import os
import logging
import fitz  # PyMuPDF
from docx import Document
from openpyxl import Workbook
from pptx import Presentation

# Imposta la configurazione del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def trascrizione(file_path, output_format="txt"):
    logging.info(f"[TRASCRIZIONE] Elaboro il file: {file_path}")
    doc = fitz.open(file_path)
    pages_text = [page.get_text() for page in doc]
    doc.close()

    output_format = output_format.lower()
    base_name = os.path.splitext(os.path.basename(file_path))[0].replace(" ", "_")
    output_path = f"{base_name}_trascrizione.{output_format}"

    if output_format == "txt":
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(pages_text))

    elif output_format == "docx":
        document = Document()
        for text in pages_text:
            document.add_paragraph(text)
            document.add_page_break()
        document.save(output_path)

    elif output_format == "xlsx":
        wb = Workbook()
        ws = wb.active
        ws.title = "PDF Testo"
        for i, text in enumerate(pages_text, start=1):
            ws.cell(row=i, column=1, value=text)
        wb.save(output_path)

    elif output_format == "pptx":
        prs = Presentation()
        blank_slide_layout = prs.slide_layouts[1]  # titolo + contenuto
        for i, text in enumerate(pages_text, start=1):
            slide = prs.slides.add_slide(blank_slide_layout)
            slide.shapes.title.text = f"Pagina {i}"
            slide.placeholders[1].text = text
        prs.save(output_path)

    else:
        logging.error(f"❌ Formato di output non supportato: {output_format}")
        return

    logging.info(f"✅ Trascrizione completata. File salvato come: {output_path}")
    print(output_path)  # utile per Colab per trovare il file

def traduzione(file_path):
    logging.info(f"[TRADUZIONE] Elaboro il file: {file_path}")
    # Da implementare
    pass

def sintesi(file_path):
    logging.info(f"[SINTESI] Elaboro il file: {file_path}")
    # Da implementare
    pass

def parse_args():
    parser = argparse.ArgumentParser(description="PDF Tool - Trascrizione, Traduzione, Sintesi")
    parser.add_argument('--action', type=str, required=True, help="Azione da eseguire: transcribe, translate, summarize")
    parser.add_argument('--file', type=str, required=True, help="Percorso del file PDF")
    parser.add_argument('--output', type=str, default="txt", help="Formato di output: txt, docx, xlsx, pptx")
    return parser.parse_args()

def main():
    args = parse_args()
    file_path = args.file.strip('"')

    if not os.path.exists(file_path):
        logging.error(f"Errore: il file {file_path} non esiste.")
        return

    if args.action == "transcribe":
        trascrizione(file_path, args.output)
    elif args.action == "translate":
        traduzione(file_path)
    elif args.action == "summarize":
        sintesi(file_path)
    else:
        logging.error(f"Azione non valida: {args.action}")

if __name__ == "__main__":
    main()
