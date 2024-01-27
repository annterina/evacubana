import os
import pathlib

from dotenv import load_dotenv

base_dir = pathlib.Path(__file__).parent.parent.parent

load_dotenv(base_dir.joinpath('.env'))


class Config:
    DEV = os.getenv('DEV', False)
    DB_REGION_NAME = os.getenv('DB_REGION_NAME')
    DB_ACCESS_KEY_ID = os.getenv('DB_ACCESS_KEY_ID')
    DB_SECRET_ACCESS_KEY = os.getenv('DB_SECRET_ACCESS_KEY')
