__version__ = '0.0.1'

from dotenv import load_dotenv, find_dotenv
from os.path import dirname

ROOT_PATH = dirname(__file__)

load_dotenv(find_dotenv())
