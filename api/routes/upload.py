from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "rag/documents"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Here you would call RAG embedding update
    # Example:
    # rag_service.add_document(file_path)

    return {"message": "Document uploaded successfully", "filename": file.filename}