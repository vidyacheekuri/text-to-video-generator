import os
# Import the OpenAI class and the specific error classes you need to handle
from openai import OpenAI, APIError, RateLimitError
from api_key import API_KEY

# --- Main Script ---
def main():
    """
    Main function to generate text based on user input and save it to a file.
    """
    try:
        # 1. Initialize the OpenAI Client
        client = OpenAI(api_key=API_KEY)

        # 2. Get user input for the topic
        prompt = input("What topic you want to write about: ")
        if not prompt:
            print("Prompt cannot be empty.")
            return

        print("\nThe AI is generating text for you...")

        # 3. Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes clear and concise text on a given topic."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.7,
        )

        # 4. Extract the generated text
        generated_text = response.choices[0].message.content

        # 5. Save the text to a file
        output_filename = "GenAI/generated_text.txt"
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(generated_text.strip())

        print(f"\nSuccess! The text has been saved to '{output_filename}'")

    # The 'except' block now correctly references the imported error classes
    except (APIError, RateLimitError) as e:
        print(f"An OpenAI API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
'''import openai
import re
from api_key import API_KEY

openai.api_key = API_KEY

# Set the model to use
model_engine = "gpt-3.5-turbo-instruct"

# Set the prompt to generate text for
text = input("What topic you want to write about: ")
prompt = text

print("The AI BOT is trying now to generate a new text for you...")
# Generate text using the GPT-3 model
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated text
generated_text = completions.choices[0].text

# Save the text in a file
with open("generated_text.txt", "w") as file:
    file.write(generated_text.strip())

print("The Text Has Been Generated Successfully!")'''
