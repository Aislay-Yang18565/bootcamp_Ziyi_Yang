from os import getenv
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file"""
    load_dotenv()

def get_key(key_name: str) -> str:
    """Get environment variable value"""
    return getenv(key_name)