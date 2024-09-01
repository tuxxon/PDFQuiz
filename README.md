# PDFQuiz

PDFQuiz is an application designed to automatically generate quizzes from PDF documents and allow users to interact with these quizzes through a web interface. The project consists of a FastAPI server and a React-based client.

## 1. Introduction

PDFQuiz allows users to upload a PDF document, analyze its content, and automatically generate quizzes using GPT-3.5. This application is particularly useful for creating quizzes from educational materials or study resources quickly and efficiently.

## 2. Features

- **PDF Upload**: Users can upload a PDF file to the application.
- **Automatic Quiz Generation**: The uploaded PDF is processed to extract text, and GPT-3.5 is utilized to generate quizzes automatically.
- **Interactive Quiz**: Users can take the generated quiz and receive immediate feedback on their answers.
- **Quiz Download**: Users can download the generated quiz as a PDF file.
- **SSE Support**: The application provides Server-Sent Events (SSE) for real-time monitoring of the quiz generation process.

## 3. Tech Stack

### Server
- **Python 3.9+**
- **FastAPI**: Web framework for building the server.
- **Uvicorn**: ASGI server for FastAPI.
- **LangChain**: Used for PDF processing and text analysis.
- **pypdf**: Library for handling PDF files.
- **fpdf**: Library for generating PDF files.

### Client
- **React**: Frontend framework for building the user interface.
- **Axios**: HTTP client for making requests to the server.

### Others
- **Docker**: Containerization platform for deploying the application.
- **Docker Compose**: Tool for defining and running multi-container Docker applications.

## 4. How to Run

### Prerequisites

- Ensure that **Docker** and **Docker Compose** are installed on your system.

### Local Setup

1. **Clone the repository**:

   ```bash
   $ git clone https://github.com/yourusername/PDFQuiz.git
   $ cd PDFQuiz
   ```

2. Build and start the application:

   ```
   $ docker-compose up --build
   ```

3. Access the application:

- Server: Access the FastAPI server at http://localhost:8000 in your browser.
- Client: Access the React client application at http://localhost:3000 in your browser.