from pathlib import Path


class PromptService:

    @staticmethod
    def load_prompt(filename: str):

        prompt_path = (
            Path(__file__).parent.parent
            / "prompts"
            / filename
        )

        return prompt_path.read_text(
            encoding="utf-8"
        )

    @staticmethod
    def build_resume_analysis_prompt(
        resume_text: str,
        job_description: str,
        ats_result: dict,
        jd_result: dict,
    ):

        prompt = PromptService.load_prompt(
            "resume_analysis.txt"
        )

        return prompt.format(
            resume=resume_text,
            job_description=job_description,
            ats_score=ats_result["ats_score"],
            matched_skills=", ".join(
                jd_result["matched_skills"]
            ),
            missing_skills=", ".join(
                jd_result["missing_skills"]
            )
        )