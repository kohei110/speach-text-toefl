import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

api_key = os.getenv('OPENAI_API_KEY')
print(api_key)