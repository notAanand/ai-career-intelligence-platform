from app.services.nlp_service import NLPService


class JDMatchService:

    @staticmethod
    def compare(resume_skills: list[str], job_description: str):

        jd_analysis = NLPService.analyze(job_description)

        jd_skills = jd_analysis["skills"]

        matched = [
            skill for skill in resume_skills
            if skill in jd_skills
        ]

        missing = [
            skill for skill in jd_skills
            if skill not in resume_skills
        ]

        score = 0

        if jd_skills:
            score = round((len(matched) / len(jd_skills)) * 100)

        return {
            "match_score": score,
            "matched_skills": matched,
            "missing_skills": missing
        }