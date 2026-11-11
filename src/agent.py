import json
from anthropic import Anthropic
from dotenv import load_dotenv

MODEL = "claude-haiku-5-5"

EXTRACTION_PROMPT = """Extract the requirements from the client brief below. Return ONLY a JSON object with these keys:
- "project_type": type of project (e.g. "exhibition stand"), or null
- "dimensions": size as text (e.g. "6 x 4 m"), or null
- "items": list of objects with "name" and "quantity"
- "date": exact event date or date range (e.g. "12-14 March 2027"), or null if the date is vague (e.g. "next spring", "soon")

- "budget": budget as text, or null
- "location": city, or null
Use null when the information is missing.
Do not guess.

Brief:
"""

load_dotenv()
client = Anthropic()

def read_brief(path):
    with open(path, encoding="utf-8") as file:
        return file.read()


def extract_requirements(brief_text):
    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=[{"role": "user", "content": EXTRACTION_PROMPT + brief_text}]
    )
    for block in response.content:
        if block.type == "text":
            return block.text
    return None


def parse_requirements(raw_text):
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        text = text.removeprefix("json")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("Error: the model did not return valid JSON.")
        print(raw_text)
        return None

CRITICAL_FIELDS = ["project_type", "date", "location"]


def find_missing_fields(requirements):
    missing = []
    for field in CRITICAL_FIELDS:
        if requirements.get(field) is None:
            missing.append(field)
    if requirements.get("dimensions") is None and not requirements.get("items"):
        missing.append("dimensions or items")
    return missing


brief = read_brief("briefs/brief_2.txt")
raw_text = extract_requirements(brief)
requirements = parse_requirements(raw_text)
print(json.dumps(requirements, indent=2))
missing = find_missing_fields(requirements)
print(missing)