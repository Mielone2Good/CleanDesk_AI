import pymupdf
from pymupdf import FileNotFoundError as PyMuPDFFileNotFound
import os

def read_document(path: str) -> dict:
    """
    get text from any document.
    """
    match path.split('.')[-1].lower():
        case 'txt':
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
                return {'text': text, 'status':'ok', 'path': path}

        case 'pdf':
            try:
                doc = pymupdf.open(path)     
                main_page = doc.load_page(0)
                return {'text': main_page.get_text(), 'status':'ok', 'path': path}
            
            except PyMuPDFFileNotFound:
                return {'error':'document not found', 'status':'error', 'path': path}


def read_dir(path: str) -> dict:
    """
    Read all documents in a folder
    return dict with all documents texts, paths and file_names
    """
    documents = {}
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            document_text = read_document(file_path)
            file_name = os.path.basename(file_path)
            if document_text['status'] == 'ok':
                documents[file_name] = [document_text['text'], file_path]
    
    return documents

