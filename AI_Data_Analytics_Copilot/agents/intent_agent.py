from services.llm_service import LLMService


class IntentAgent:

    def __init__(self):
        self.llm = LLMService()

    def detect(self, question):

        prompt = f"""
You are an Intent Classifier.

Your job is to classify the user's question.

Return ONLY one word.

QUERY
or
INSIGHT

Examples

Question:
Top 10 customers
Answer:
QUERY

Question:
Highest sales city
Answer:
QUERY

Question:
Average discount
Answer:
QUERY

Question:
Why Surat sales are low?
Answer:
INSIGHT

Question:
Why profit decreased?
Answer:
INSIGHT

Question:
Compare Delhi and Mumbai sales.
Answer:
INSIGHT

Question:
Give recommendations to improve sales.
Answer:
INSIGHT

User Question:
{question}
"""

        result = self.llm.generate(prompt)

        return result.strip().upper()