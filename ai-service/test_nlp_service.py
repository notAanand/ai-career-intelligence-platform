from app.services.nlp_service import NLPService

sample_text = """
Anand Singh

Email : anand@gmail.com

Phone : +91 9876543210

Skills :
Python
React
Node.js
MongoDB
Machine Learning
Docker
GitHub
"""

result = NLPService.analyze(sample_text)

print(result)