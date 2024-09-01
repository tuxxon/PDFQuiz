import os
import json
from fpdf import FPDF
from utils.quiz_utils import pdf_to_quiz, generate_questions

async def generate_quiz_from_pdf(pdf_file: str) -> str:
    # PDF에서 퀴즈 생성
    questions = await pdf_to_quiz(pdf_file)

    if not questions:
        raise ValueError("No questions were generated from the PDF")

    # 퀴즈를 JSON 파일로 저장
    quiz_json_path = pdf_file.replace(".pdf", ".json")
    with open(quiz_json_path, "w") as json_file:
        json.dump(questions, json_file, ensure_ascii=False, indent=4)  # JSON 파일을 읽기 쉽게 저장

    return quiz_json_path

async def generate_pdf_from_quiz(quiz_file: str) -> str:
    # JSON 파일에서 퀴즈 데이터를 로드
    pdf_file_path = quiz_file.replace(".json", ".pdf")
    with open(quiz_file, "r", encoding='utf-8') as json_file:
        quiz_data = json.load(json_file)

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)  # 자동 페이지 브레이크 설정
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        # 퀴즈 데이터를 기반으로 PDF 생성
        generate_questions(quiz_data, pdf, print_response=False)
        generate_questions(quiz_data, pdf, print_response=True)

        pdf.output(pdf_file_path, 'F')  # PDF 파일로 저장

    return pdf_file_path
