from agents.intent_agent import IntentAgent

agent = IntentAgent()

print(agent.detect("Top 5 Customers"))

print(agent.detect("Why Surat sales are low"))

print(agent.detect("Compare Delhi and Mumbai"))

print(agent.detect("Average Discount"))