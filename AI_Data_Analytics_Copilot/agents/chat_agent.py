from agents.query_agent import QueryAgent
from agents.insight_agent import InsightAgent
from agents.intent_agent import IntentAgent


class ChatAgent:

    def __init__(self):

        self.query_agent = QueryAgent()
        self.insight_agent = InsightAgent()
        self.intent_agent = IntentAgent()

    def ask(self, df, question):

        intent = self.intent_agent.detect(question)

        print("Detected Intent :", intent)

        if "INSIGHT" in intent:

            return self.insight_agent.ask(df, question)

        return self.query_agent.ask(df, question)