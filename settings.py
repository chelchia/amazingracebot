import os
from dotenv import load_dotenv, find_dotenv

#dotenv_path = join(dirname(__file__), '.env')
#load_dotenv(dotenv_path)
#load_dotenv()
load_dotenv(find_dotenv())

token = os.environ.get("TOKEN")

