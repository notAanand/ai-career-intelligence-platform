import re
import spacy

from app.utils.constants import SKILLS

nlp = spacy.load("en_core_web_sm")


class NLPService:

    @staticmethod
    def extract_email(text: str):

        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        return match.group() if match else None

    @staticmethod
    def extract_phone(text: str):

        match = re.search(
            r"(\+91[\-\s]?)?[6-9]\d{9}",
            text,
        )

        return match.group() if match else None

    @staticmethod
    def extract_skills(text: str):

        found = []

        lower = text.lower()

        for skill in SKILLS:

            if skill.lower() in lower:
                found.append(skill)

        return sorted(set(found))

    @staticmethod
    def extract_github(text: str):

        import re

        match = re.search(
            r"https?://(?:www\.)?github\.com/[A-Za-z0-9_.-]+",
            text,
            re.IGNORECASE
        )
    @staticmethod
    def extract_linkedin(text: str):

        import re

        match = re.search(
            r"https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?",
            text,
            re.IGNORECASE
    )

        return match.group() if match else None

    @staticmethod
    def analyze(text: str):

        return {
    "email": NLPService.extract_email(text),
    "phone": NLPService.extract_phone(text),
    "skills": NLPService.extract_skills(text),
    "github": NLPService.extract_github(text),
    "linkedin": NLPService.extract_linkedin(text)
}