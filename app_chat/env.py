import os
from dotenv import load_dotenv
from pathlib import Path

BASE_CODE_DIR = Path(__file__).resolve().parent.parent

# Load variables from .env file
load_dotenv(BASE_CODE_DIR / '.env')


# DB
DB_HOST = os.getenv('DB_HOST', None)
assert DB_HOST

DB_PORT = os.getenv('DB_PORT', None)
assert DB_PORT

DB_NAME = os.getenv('DB_NAME', None)
assert DB_NAME

DB_USER = os.getenv('DB_USER', None)
assert DB_USER

DB_PASSWORD = os.getenv('DB_PASSWORD', None)
assert DB_PASSWORD

# REDIS
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
assert REDIS_HOST

REDIS_PORT = os.getenv('REDIS_PORT', 6379)
assert REDIS_PORT
