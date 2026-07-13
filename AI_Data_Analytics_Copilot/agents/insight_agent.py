from services.llm_service import LLMService
from services.analysis_service import AnalysisService


class InsightAgent:

    def __init__(self):
        self.llm = LLMService()

    # =====================================================
    # AI INSIGHTS (Dashboard Section)
    # =====================================================

    def generate(self, df, profile):

        analysis = AnalysisService.analyze(df)

        prompt = f"""
You are a Senior Business Data Analyst.

Generate a professional business report.

=========================
DATASET INFORMATION
=========================

Rows:
{len(df)}

Columns:
{list(df.columns)}

Numeric Columns:
{profile['numeric']}

Categorical Columns:
{profile['categorical']}

Datetime Columns:
{profile['datetime']}

=========================
ANALYSIS
=========================

City Sales

{analysis.get("city_sales","Not Available")}

Orders by City

{analysis.get("city_orders","Not Available")}

Category Sales

{analysis.get("category_sales","Not Available")}

Payment Mode

{analysis.get("payment_mode","Not Available")}

Order Status

{analysis.get("order_status","Not Available")}

=========================

Return ONLY markdown.

Create sections:

# Executive Summary

# Key Business Insights

# Data Quality

# Recommendations

# Conclusion
"""

        return self.llm.generate(prompt)

    # =====================================================
    # CHATBOT INSIGHTS
    # =====================================================

    def ask(self, df, question):

        analysis = AnalysisService.analyze(df)

        prompt = f"""
You are a Senior Business Data Analyst.

Answer ONLY using the dataset analysis below.

=========================
USER QUESTION
=========================

{question}

=========================
DATASET
=========================

Rows:
{len(df)}

Columns:
{list(df.columns)}

=========================
CITY SALES
=========================

{analysis.get("city_sales","Not Available")}

=========================
CITY ORDERS
=========================

{analysis.get("city_orders","Not Available")}

=========================
CATEGORY SALES
=========================

{analysis.get("category_sales","Not Available")}

=========================
PAYMENT MODE
=========================

{analysis.get("payment_mode","Not Available")}

=========================
ORDER STATUS
=========================

{analysis.get("order_status","Not Available")}

=========================
RULES
=========================

1. Never invent values.
2. Never guess.
3. Use ONLY the data above.
4. If information is unavailable, clearly say so.
5. Answer in simple business language.
6. Give bullet points whenever possible.
7. End with a recommendation.

Return markdown only.
"""

        answer = self.llm.generate(prompt)

        return {
            "success": True,
            "type": "insight",
            "result": answer
        }