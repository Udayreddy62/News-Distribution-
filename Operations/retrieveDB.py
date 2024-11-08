import os

from dotenv import load_dotenv

 

class Environment:

    load_dotenv()

    database_url = os.environ.get('DATABASE_URL')
