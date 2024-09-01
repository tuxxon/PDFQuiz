from fastapi import APIRouter, UploadFile, File, HTTPException
from services.file_service import save_uploaded_file

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    pdf_path = await save_uploaded_file(file, destination_dir="./pdfs")
    return {"message": "PDF uploaded successfully", "pdf_file": pdf_path}
