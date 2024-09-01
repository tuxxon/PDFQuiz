import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from services.pdf_service import generate_pdf_from_quiz

router = APIRouter()

@router.get("/download_quiz")
async def download_quiz(quiz_file: str):
    if not os.path.exists(quiz_file):
        raise HTTPException(status_code=404, detail="Quiz file not found")

    pdf_file_path = await generate_pdf_from_quiz(quiz_file)
    return FileResponse(pdf_file_path, media_type='application/pdf', filename=os.path.basename(pdf_file_path))
