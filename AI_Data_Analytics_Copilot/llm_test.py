from services.llm_service import LLMService

llm = LLMService()

response = llm.generate("Say Hello in one line.")

print(response)