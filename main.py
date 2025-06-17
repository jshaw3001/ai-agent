import sys
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main(prompt):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    print(response.text)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <prompt>")
    sys.exit(1)