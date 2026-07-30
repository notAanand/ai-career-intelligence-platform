import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.schemas.resume_schema import ResumeResponse
from app.services.pdf_parser import PDFParser

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_FOLDER = "uploads"


@router.post(
    "/upload",
    response_model=ResumeResponse
)
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = PDFParser.extract_text(file_path)

    return ResumeResponse(
        filename=file.filename,
        extracted_text=extracted_text
    )