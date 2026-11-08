from anthropic import Anthropic
from dotenv import load_dotenv

MODEL = "claude-haiku-5-5"

load_dotenv()
client = Anthropic()

response = client.messages.create(
    model=MODEL,
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Say hello to an event construction engineer in one sentence."}
    ],
)


print(response.content[0].text)