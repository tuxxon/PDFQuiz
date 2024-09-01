import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = ({ onUploadSuccess }) => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        if (!selectedFile) return;

        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await axios.post('http://localhost:8000/upload_pdf', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            // Verify that the response contains the correct path and call the callback
            console.log(`[debug] upload response = ${JSON.stringify(response.data)}`);
            if (response.data && response.data.pdf_file) {
                onUploadSuccess(response.data.pdf_file);
            } else {
                console.error("Unexpected response structure:", response);
            }
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload PDF</button>
        </div>
    );
};

export default FileUpload;
