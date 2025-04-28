# src/main.py

import argparse
import os

def trascrizione(file_path):
    print(f"[TRASCRIZIONE] Elaboro il file: {file_path}")
    # Qui andrà il codice per la trascrizione
    pass

def traduzione(file_path):
    print(f"[TRADUZIONE] Elaboro il file: {file_path}")
    # Qui andrà il codice per la traduzione
    pass

def sintesi(file_path):
    print(f"[SINTESI] Elaboro il file: {file_path}")
    # Qui andrà il codice per la sintesi
    pass

def main():
    parser = argparse.ArgumentParser(description="PDF Tool - Trascrizione, Traduzione, Sintesi")
    parser.add_argument('--action', type=str, required=True, help="Azione da eseguire: transcribe, translate, summarize")
    parser.add_argument('--file', type=str, required=True, help="Percorso del file PDF")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Errore: il file {args.file} non esiste.")
        return

    if args.action == "transcribe":
        trascrizione(args.file)
    elif args.action == "translate":
        traduzione(args.file)
    elif args.action == "summarize":
        sintesi(args.file)
    else:
        print(f"Azione non valida: {args.action}")

if __name__ == "__main__":
    main()
