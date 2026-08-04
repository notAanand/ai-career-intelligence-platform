from app.services.pdf_parser import PDFParser
from app.services.nlp_service import NLPService
from app.services.jd_match_service import JDMatchService
from app.services.ats_service import ATSService
from app.services.prompt_service import PromptService
from app.services.gemini_service import GeminiService


class AnalysisService:

    @staticmethod
    def analyze_resume(
        file_path: str,
        job_description: str
    ):

        # Step 1
        resume_text = PDFParser.extract_text(file_path)

        # Step 2
        resume_analysis = NLPService.analyze(
            resume_text
        )

        # Step 3
        jd_analysis = JDMatchService.compare(
            resume_analysis["skills"],
            job_description
        )

        # Step 4
        ats_analysis = ATSService.calculate(
            resume_analysis,
            resume_text
        )

        # Step 5
        prompt = PromptService.build_resume_analysis_prompt(
            resume_text=resume_text,
            job_description=job_description,
            ats_result=ats_analysis,
            jd_result=jd_analysis,
        )

        # Step 6
        gemini = GeminiService()

        ai_feedback = gemini.generate_json(
            prompt
        )

        return {
    "success": True,
    "message": "Resume analyzed successfully",
    "data": {
        "candidate": resume_analysis,
        "analysis": {
            "ats": ats_analysis,
            "job_match": jd_analysis,
            "ai_feedback": ai_feedback
        }
    }
}