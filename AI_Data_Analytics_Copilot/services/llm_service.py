import os
import streamlit as st
from openai import OpenAI


class LLMService:

    def __init__(self):

        # First try environment variable
        api_key = os.getenv("GROQ_API_KEY")

        # If not found, use Streamlit Secrets
        if not api_key:
            api_key = st.secrets["GROQ_API_KEY"]

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        self.model = "llama-3.3-70b-versatile"

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content
