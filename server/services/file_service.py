import os
from fastapi import UploadFile

async def save_uploaded_file(file: UploadFile, destination_dir: str) -> str:
    os.makedirs(destination_dir, exist_ok=True)
    file_path = os.path.join(destination_dir, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return file_path
