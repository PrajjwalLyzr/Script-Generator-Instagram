import os
from lyzr import Generator
import google.generativeai as genai
from dotenv import load_dotenv; load_dotenv()

# setup Google api key to use Gemini-Pro
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

def script_generator(API_KEY, user_input, reference=''):
    generator = Generator(api_key=API_KEY)
    if reference == '':
        script = generator.generate(text=user_input,instructions=f'Instagram Reel script for 60 seconds video, having the timestamp, visuals and voice over for each scence. [!Important] avoid reponse intro and conclusion')
    else:
        script = generator.generate(text=user_input,instructions=f'Instagram Reel script for 60 seconds video, having the timestamp, visuals and voice over for each scence. You can Use this refrence: "{reference}". [!Important] avoid reponse intro and conclusion')
    return script


def script_finetuner(first_draft):
    prompt = f"""
                Fine-tune this: "{first_draft}" Instagram reel script to make it more engaging and attractive to various audiences. [!Important]. Avoid the introduction and conclusion text of the response.
                Use this template for script:

                
                [00:00 - 00:05]
                - Visual: 
                - Voiceover: 

                [00:05 - 00:10]
                - Visual: 
                - Voiceover: 

                [00:10 - 00:17]
                - Visual: 
                - Voiceover: 

                [00:17 - 00:20]
                - Visual: 
                - Voiceover: 

                [00:20 - 00:30]
                - Visual: 
                - Voiceover: 

                [00:30 - 00:40]
                - Visual: 
                - Voiceover: 

                [00:40 - 00:50]
                - Visual: 
                - Voiceover: 

                [00:50 - 01:00]
                - Visual: 
                - Voiceover: 
            
                """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response

# Function to handle the addition of the OpenAI API key
def save_api_key(key):
    with open("api_key.txt", "w") as file:
        file.write(key)

# Function to handle example text submission
def save_example(text):
    with open("examples.txt", "a") as file:
        file.write(text + "\n")

# Function to generate script based on user instruction
def generate_script(instruction, refrence=None):
    with open('api_key.txt', 'r') as file:
        api_key = file.read()
    api_key = api_key.replace(" ", "")
    draft = script_generator(API_KEY=api_key, user_input=instruction, reference=refrence)
    final_script = script_finetuner(first_draft=draft)
    # This should call the OpenAI API using the instruction
    # Placeholder for API call
    return final_script.text

# Function to save edited prompt
def save_prompt(text):
    with open("prompt.txt", "a") as file:
        file.write(text)


