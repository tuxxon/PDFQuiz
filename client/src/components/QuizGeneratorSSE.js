import React, { useState } from 'react';

const QuizGeneratorSSE = ({ pdfFile }) => {
    const [messages, setMessages] = useState([]);

    const startSSE = () => {
        const eventSource = new EventSource(`http://localhost:8000/generate_quiz_sse?pdf_file=${encodeURIComponent(pdfFile)}`);

        eventSource.onmessage = (event) => {
            setMessages(prev => [...prev, event.data]);
        };

        eventSource.onerror = (error) => {
            console.error('EventSource failed:', error);
            eventSource.close();
        };
    };

    return (
        <div>
            <button onClick={startSSE}>Generate Quiz with SSE</button>
            <div>
                {messages.map((msg, index) => (
                    <p key={index}>{msg}</p>
                ))}
            </div>
        </div>
    );
};

export default QuizGeneratorSSE;
