import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

parser = argparse.ArgumentParser(description="ai-agent")
parser.add_argument('user_prompt', type=str, help="User prompt")
parser.add_argument('--verbose', action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("api-key not found")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

if not response or not response.usage_metadata:
    raise RuntimeError("response seems to have failed")

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
print(response.text)