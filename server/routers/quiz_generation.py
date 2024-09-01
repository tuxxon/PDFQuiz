import asyncio
import os
import json
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Request
from services.pdf_service import generate_quiz_from_pdf

router = APIRouter()

class QuizRequest(BaseModel):
    pdf_file: str

@router.post("/generate_quiz")
async def generate_quiz(request: QuizRequest):

    pdf_file = request.pdf_file
    
    if not os.path.exists(pdf_file):
        raise HTTPException(status_code=404, detail="PDF file not found")

    quiz_json_path = await generate_quiz_from_pdf(pdf_file)
    
    # JSON 파일의 내용을 읽어서 반환
    with open(quiz_json_path, "r", encoding='utf-8') as json_file:
        quiz_data = json.load(json_file)

    return {"message": "Quiz generated successfully", "quiz_data": quiz_data, "quiz_file": quiz_json_path}

async def generate_quiz_sse(request: Request, pdf_file: str):
    async def event_generator():
        # 퀴즈 생성 시작
        yield "data: Starting quiz generation...\n\n"
        await asyncio.sleep(1)  # 작업 시뮬레이션

        quiz_json_path = await generate_quiz_from_pdf(pdf_file)
        yield f"data: Quiz generated. Path: {quiz_json_path}\n\n"

        with open(quiz_json_path, "r", encoding='utf-8') as json_file:
            quiz_data = json.load(json_file)
            yield f"data: {json.dumps(quiz_data)}\n\n"

        yield "data: Quiz generation completed.\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

@router.get("/generate_quiz_sse")
async def generate_quiz(pdf_file: str):
    return await generate_quiz_sse(Request, pdf_file)