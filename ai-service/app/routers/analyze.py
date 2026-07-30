from fastapi import APIRouter
from pydantic import BaseModel
from app.services.jd_match_service import JDMatchService

router = APIRouter(prefix="/analyze", tags=["Analysis"])


class AnalyzeRequest(BaseModel):
    resume_skills: list[str]
    job_description: str


@router.post("/")
def analyze(request: AnalyzeRequest):

    result = JDMatchService.compare(
        request.resume_skills,
        request.job_description
    )

    return result