import os
from dotenv import load_dotenv
from google import genai
import argparse

parser = argparse.ArgumentParser(description="ai-agent")
parser.add_argument('user_prompt', type=str, help="User prompt")
args = parser.parse_args()

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("api-key not found")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(model="gemini-2.5-flash", contents=args.user_prompt)

if not response or not response.usage_metadata:
    raise RuntimeError("response seems to have failed")

print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(response.text)