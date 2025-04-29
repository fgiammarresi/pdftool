# src/main.py

import argparse
import os
import logging

# Imposta la configurazione del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def trascrizione(file_path):
    logging.info(f"[TRASCRIZIONE] Elaboro il file: {file_path}")
    # Qui andrà il codice per la trascrizione
    pass

def traduzione(file_path):
    logging.info(f"[TRADUZIONE] Elaboro il file: {file_path}")
    # Qui andrà il codice per la traduzione
    pass

def sintesi(file_path):
    logging.info(f"[SINTESI] Elaboro il file: {file_path}")
    # Qui andrà il codice per la sintesi
    pass

def parse_args():
    parser = argparse.ArgumentParser(description="PDF Tool - Trascrizione, Traduzione, Sintesi")
    parser.add_argument('--action', type=str, required=True, help="Azione da eseguire: transcribe, translate, summarize")
    parser.add_argument('--file', type=str, required=True, help="Percorso del file PDF")
    return parser.parse_args()

def main():
    # Analizza gli argomenti
    args = parse_args()

    # Gestione dei file con spazi (aggiungi virgolette per evitare problemi di separazione degli argomenti)
    file_path = args.file
    if " " in file_path:
        file_path = f'"{file_path}"'

    # Verifica se il file esiste
    if not os.path.exists(file_path.strip('"')):
        logging.error(f"Errore: il file {file_path} non esiste.")
        return

    # Esegui l'azione richiesta
    if args.action == "transcribe":
        trascrizione(file_path)
    elif args.action == "translate":
        traduzione(file_path)
    elif args.action == "summarize":
        sintesi(file_path)
    else:
        logging.error(f"Azione non valida: {args.action}")

if __name__ == "__main__":
    main()
