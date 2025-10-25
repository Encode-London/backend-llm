import argparse
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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"
)

class AiScore(BaseModel):
    score: float
    reasons: list[str]

def read_file(filename):
    #Read and return the content of a file, or None if not found or empty.
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
        if not content:
            print(f"Error: {filename} is empty.")
            return None
        return content
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None


def main():
    # read files
    prompt_content = read_file('prompt.txt')
    if prompt_content is None:
        return
    data_content = read_file('data.txt')
    if data_content is None:
        return


    # Send the prompt to OpenAI API
    try:
        completion = client.responses.parse(
            model="openai/gpt-oss-20b:free",  # Or another model available via OpenRouter
            input=[
                {
                    "role": "system",
                    "content": prompt_content
                    },
                {
                    "role": "user",
                    "content": data_content
                },
            ],
            text_format=AiScore,
                       
        )

        text = completion.output_parsed
        print(text)
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")

if __name__ == "__main__":
    main()