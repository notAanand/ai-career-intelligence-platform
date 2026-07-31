from app.services.pdf_parser import PDFParser
from app.services.nlp_service import NLPService
from app.services.jd_match_service import JDMatchService
from app.services.ats_service import ATSService


class AnalysisService:

    @staticmethod
    def analyze_resume(file_path: str, job_description: str):

        # Step 1: Extract text from resume
        resume_text = PDFParser.extract_text(file_path)

        # Step 2: Analyze resume using NLP
        resume_analysis = NLPService.analyze(resume_text)

        # Step 3: Compare resume with Job Description
        jd_analysis = JDMatchService.compare(
            resume_analysis["skills"],
            job_description
        )

        # Step 4: Calculate ATS Score
        ats_analysis = ATSService.calculate(
            resume_analysis,
            resume_text
        )

        # Step 5: Return Complete Analysis
        return {
            "candidate": {
                "email": resume_analysis["email"],
                "phone": resume_analysis["phone"],
                "skills": resume_analysis["skills"]
            },
            "job_match": {
                "match_score": jd_analysis["match_score"],
                "matched_skills": jd_analysis["matched_skills"],
                "missing_skills": jd_analysis["missing_skills"]
            },
            "ats": {
                "ats_score": ats_analysis["ats_score"],
                "breakdown": ats_analysis["breakdown"]
            }
        }