from pydantic import BaseModel


class Candidate(BaseModel):
    email: str | None = None
    phone: str | None = None
    skills: list[str]


class JobMatch(BaseModel):
    match_score: int
    matched_skills: list[str]
    missing_skills: list[str]


class AnalysisResponse(BaseModel):
    candidate: Candidate
    job_match: JobMatch