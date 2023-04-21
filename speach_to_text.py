import openai
import os
from dotenv import load_dotenv
import sys

load_dotenv() 
api_key = os.getenv('OPENAI_API_KEY')

file_path = sys.argv[1]
print(file_path)