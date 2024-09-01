import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import QuizGenerator from './components/QuizGenerator';
import QuizGeneratorSSE from './components/QuizGeneratorSSE';  // SSE 컴포넌트 임포트

const App = () => {
    const [pdfFile, setPdfFile] = useState(null);

    const handleUploadSuccess = (uploadedPdfFile) => {
        console.log("File uploaded successfully, path:", uploadedPdfFile); // Debugging line
        setPdfFile(uploadedPdfFile);
    };

    return (
        <div>
            <h1>PDF to Quiz Generator</h1>
            <FileUpload onUploadSuccess={handleUploadSuccess} />
            {pdfFile ? (
                <>
                    <QuizGenerator pdfFile={pdfFile} />
                    {/* <QuizGeneratorSSE pdfFile={pdfFile} />  SSE 방식 추가 */}
                </>
            ) : (
                <p>Waiting for file upload...</p>
            )}
        </div>
    );
};

export default App;
