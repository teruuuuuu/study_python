import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Fablic setting
FABLIC_HOST = os.environ.get("FABLIC_HOST")
FABLIC_PORT = 22
FABLIC_USER = os.environ.get("FABLIC_USER")
FABLIC_PASSWORD = os.environ.get("FABLIC_PASSWORD")
FABLIC_KEY_FILE = os.environ.get("FABLIC_KEY_FILE")

# Pymongo setting
PYMONGO_HOST = os.environ.get("PYMONGO_HOST")
PYMONGO_DB = os.environ.get("PYMONGO_DB")