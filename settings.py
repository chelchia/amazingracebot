import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

token = os.environ.get("TOKEN")

