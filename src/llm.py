import argparse
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",

)

def main():
    # Read the entire content from prompt.txt
    try:
        with open('prompt.txt', 'r') as f:
            prompt_content = f.read().strip()
    except FileNotFoundError:
        print("Error: prompt.txt not found.")
        return
    
    if not prompt_content:
        print("Error: prompt.txt is empty.")
        return
    
    # Send the prompt to OpenAI API
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or another model available via OpenRouter
            messages=[
                {"role": "user", "content": prompt_content}
            ]
        )
        response = completion.choices[0].message.content
        print(response)
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")

if __name__ == "__main__":
    main()