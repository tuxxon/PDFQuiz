from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import upload, quiz_generation, download

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 요청을 허용, 특정 도메인만 허용하려면 ["http://example.com"]과 같이 설정
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드를 허용
    allow_headers=["*"],  # 모든 HTTP 헤더를 허용
)

# Include routers
app.include_router(upload.router)
app.include_router(quiz_generation.router)
app.include_router(download.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
