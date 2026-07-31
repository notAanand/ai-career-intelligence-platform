import re


class ATSService:

    @staticmethod
    def calculate(resume_analysis: dict, resume_text: str) -> dict:

        score = 0
        breakdown = {}

        # Contact Information (10)
        contact_score = 0

        if resume_analysis.get("email"):
            contact_score += 5

        if resume_analysis.get("phone"):
            contact_score += 5

        score += contact_score
        breakdown["contact"] = contact_score

        # Skills (30)
        skills = resume_analysis.get("skills", [])

        skill_score = min(len(skills) * 3, 30)

        score += skill_score
        breakdown["skills"] = skill_score

        # Projects (20)
        project_keywords = [
            "project",
            "projects",
            "developed",
            "built",
            "implemented"
        ]

        project_score = 20 if any(
            keyword in resume_text.lower()
            for keyword in project_keywords
        ) else 0

        score += project_score
        breakdown["projects"] = project_score

        # Education (15)
        education_keywords = [
            "b.tech",
            "bachelor",
            "university",
            "college"
        ]

        education_score = 15 if any(
            keyword in resume_text.lower()
            for keyword in education_keywords
        ) else 0

        score += education_score
        breakdown["education"] = education_score

        # Experience (15)
        experience_keywords = [
            "intern",
            "experience",
            "worked",
            "company"
        ]

        experience_score = 15 if any(
            keyword in resume_text.lower()
            for keyword in experience_keywords
        ) else 0

        score += experience_score
        breakdown["experience"] = experience_score

        # Resume Length (10)
        words = len(resume_text.split())

        if 250 <= words <= 800:
            format_score = 10
        elif 150 <= words < 250:
            format_score = 7
        else:
            format_score = 5

        score += format_score
        breakdown["format"] = format_score

        return {
            "ats_score": min(score, 100),
            "breakdown": breakdown
        }