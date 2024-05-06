import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(env_path)

class Settings:
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER  = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER  = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT  = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB  = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()

if __name__ == "__main__":
    print(settings.DATABASE_URL)
    print(settings.POSTGRES_USER)
    print(settings.POSTGRES_PASSWORD)
    print(settings.POSTGRES_SERVER)
    print(settings.POSTGRES_PORT)
    print(settings.POSTGRES_DB)
    print(settings.PROJECT_NAME)
    print(settings.PROJECT_VERSION)
    