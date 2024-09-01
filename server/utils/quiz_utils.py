import asyncio
from fpdf import FPDF
from langchain_community.document_loaders import PyPDFLoader
from .quizz_generator import generate_quizz

def transform(input_list):
    # 퀴즈 데이터를 새로운 형식으로 변환
    new_list = []
    for item in input_list:
        for key in item:
            if 'question1' in key or 'question2' in key or 'question3' in key:
                question_dict = {}
                question_num = key[-1]
                question_dict['question'] = item[key]
                question_dict['A'] = item[f'A_{question_num}']
                question_dict['B'] = item[f'B_{question_num}']
                question_dict['C'] = item[f'C_{question_num}']
                question_dict['D'] = item[f'D_{question_num}']
                question_dict['reponse'] = item[f'reponse{question_num}']
                new_list.append(question_dict)
    return new_list

async def pdf_to_quiz(pdf_file_name: str):
    # PDF 파일에서 텍스트를 추출하고 퀴즈를 생성
    loader = PyPDFLoader(pdf_file_name)
    pages = loader.load_and_split()

    sem = asyncio.Semaphore(10)  # 동시에 처리할 최대 페이지 수 제한

    async def process_page(page):
        async with sem:
            return await generate_quizz(page.page_content)

    tasks = [process_page(page) for page in pages]
    all_questions = []

    # 모든 페이지에서 생성된 퀴즈를 모아서 변환
    questions = await asyncio.gather(*tasks)
    for question in questions:
        if question and question[0]:
            all_questions.extend(transform(question[0]))
        else:
            print("Warning: A page did not generate any questions or returned None.")

    return all_questions

def generate_questions(data, pdf: FPDF, print_response: bool = False):
    # PDF에 퀴즈 데이터를 추가
    pdf.add_page()
    question_number = 1

    for question_data in data:
        question = question_data["question"]
        options = [
            f"A{question_data['A']}",
            f"B{question_data['B']}",
            f"C{question_data['C']}",
            f"D{question_data['D']}"
        ]

        # 각 질문과 답변을 PDF에 추가
        pdf.multi_cell(0, 10, f"{question_number}. {question}")
        for option in options:
            pdf.multi_cell(0, 10, option)

        response = "?"
        if print_response:
            response = question_data["reponse"]

        pdf.cell(0, 10, f"Response: {response}", ln=True)
        pdf.cell(0, 10, "", ln=True)
        question_number += 1

    pdf.add_page()
