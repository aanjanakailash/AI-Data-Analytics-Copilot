from services.llm_service import LLMService
from services.prompt_service import PromptService
from services.pandas_executor import PandasExecutor


class QueryAgent:

    def __init__(self):
        self.llm = LLMService()

    def ask(self, df, question):

        # Build Prompt
        prompt = PromptService.build_chat_prompt(df, question)

        # Generate Pandas Code
        code = self.llm.generate(prompt)

        # Remove markdown
        code = code.replace("```python", "")
        code = code.replace("```", "")
        code = code.strip()

        # Execute Code
        result, error = PandasExecutor.execute(df, code)

        if error:
            return {
                "success": False,
                "error": error,
                "code": code,
                "result": None
            }

        return {
            "success": True,
            "code": code,
            "result": result
        }