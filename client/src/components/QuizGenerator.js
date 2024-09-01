import React, { useState } from 'react';
import axios from 'axios';

const QuizGenerator = ({ pdfFile }) => {
    const [quizFile, setQuizFile] = useState(null);
    const [quizData, setQuizData] = useState(null);    
    const [error, setError] = useState(null);    
    const [userAnswers, setUserAnswers] = useState({});  // 사용자 답변 상태

    const handleGenerateQuiz = async () => {
        try {
            const response = await axios.post('http://localhost:8000/generate_quiz', { pdf_file: pdfFile });

            console.log(response.data);            
            setQuizFile(response.data.quiz_file);
            setQuizData(response.data.quiz_data);
        } catch (error) {
            console.error('Error generating quiz:', error);
            setError('Error generating quiz');
        }
    };

    const handleAnswerClick = (questionIndex, option) => {
        setUserAnswers({
            ...userAnswers,
            [questionIndex]: option
        });
    };

    const handleDownloadQuiz = () => {
        if (quizFile) {
            window.location.href = `http://localhost:8000/download_quiz?quiz_file=${encodeURIComponent(quizFile)}`;
        }
    };

    return (
        <div>
            <button onClick={handleGenerateQuiz}>Generate Quiz</button>
            {quizFile && <button onClick={handleDownloadQuiz}>Download Quiz</button>}
            {error && <p>Error: {error}</p>}
            {quizData && (
                <div>
                    <h3>Generated Quiz</h3>
                    {quizData.map((questionData, index) => (
                        <div key={index} style={{ marginBottom: '20px' }}>
                            <p>
                                {userAnswers[index] !== undefined && (
                                    userAnswers[index] === questionData.reponse ? (
                                        <span style={{ color: 'green', fontWeight: 'bold' }}>✓</span>
                                    ) : (
                                        <span style={{ color: 'red', fontWeight: 'bold' }}>✗</span>
                                    )
                                )} {index + 1}. {questionData.question}
                            </p>
                            <div>
                                {['A', 'B', 'C', 'D'].map((option) => (
                                    <div 
                                        key={option} 
                                        onClick={() => handleAnswerClick(index, option)} 
                                        style={{ 
                                            margin: '5px 0', 
                                            padding: '8px', 
                                            cursor: 'pointer', 
                                            backgroundColor: userAnswers[index] === option ? (
                                                option === questionData.reponse ? 'lightgreen' : 'salmon'
                                            ) : ''
                                        }}
                                    >
                                        {option}: {questionData[option]}
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            )}            
        </div>
    );
};

export default QuizGenerator;
