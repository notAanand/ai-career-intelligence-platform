from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os

from app.services.analysis_service import AnalysisService

router = APIRouter(
    prefix="/analysis",
    tags=["Complete Analysis"]
)


@router.post("/")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    upload_dir = "app/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, resume.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    result = AnalysisService.analyze_resume(
        file_path=file_path,
        job_description=job_description
    )

    return result