# 베이스 이미지로 Python 3.11 사용
FROM python:3.11-slim

# 작업 디렉터리 설정
WORKDIR /app

# 필요 패키지 설치를 위한 파일 복사
COPY requirements.txt .

# 필요 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY . .

# FastAPI 서버 실행 (Uvicorn 사용)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
