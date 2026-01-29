import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        sys.exit("Usage: python main.py <prompt>")
    prompt = sys.argv[1]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant. Answer briefly and friendly."),
        contents=prompt,
    )
    print(response.text)

    if response is None or response.usage_metadata is None:
        print("Usage metadata not available")
    else:
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Total Tokens: {response.usage_metadata.total_token_count}")

if __name__ == "__main__":
    main()
