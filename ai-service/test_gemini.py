from app.services.gemini_service import GeminiService
from app.services.prompt_service import PromptService

prompt = PromptService.load_prompt(
    "resume_analysis.txt"
)

prompt = prompt.format(
    resume="""
Python Developer

Skills:
Python
React
Node.js
MongoDB

Projects:
AI Resume Analyzer
Portfolio Website
""",
    job_description="""
Looking for a Python Backend Developer with FastAPI,
Docker, AWS and MongoDB.
""",
    ats_score=72,
    matched_skills=["Python", "MongoDB"],
    missing_skills=["Docker", "AWS", "FastAPI"]
)

gemini = GeminiService()

result = gemini.generate_json(prompt)

print(result)