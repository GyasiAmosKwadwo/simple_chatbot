
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def main():
    input_request = input("Enter your prompt: ")

    response = client.responses.create(
        input=input_request,
        model="openai/gpt-oss-20b",
    )
    print(response.output_text)
    main()

if __name__ == "__main__":
    main()

