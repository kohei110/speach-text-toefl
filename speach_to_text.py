import openai
import os
from dotenv import load_dotenv
import sys

load_dotenv() 
openai.api_key = os.getenv('OPENAI_API_KEY')

file_path = sys.argv[1]
audio_file = open(file_path, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print("Whisper API Output")
print(transcript.text)