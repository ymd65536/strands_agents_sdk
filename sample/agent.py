from strands import Agent
from strands.models import BedrockModel

bedrock_model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0"
)

agent = Agent(model=bedrock_model)

print("---start---")
agent("Tell me about agentic AI in Japanese.")
print("---end---")
