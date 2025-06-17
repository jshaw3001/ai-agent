import sys
import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
parser = argparse.ArgumentParser()

parser.add_argument("--verbose", action="store_true")
parser.add_argument("user_prompt", help="respond to the string you use here")

args = parser.parse_args()

def main(user_prompt):
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
    print(response.text)

main(args.user_prompt)