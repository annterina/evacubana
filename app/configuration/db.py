import os
import pathlib
import boto3
from boto3.resources.base import ServiceResource
from dotenv import load_dotenv

base_dir = pathlib.Path(__file__).parent.parent.parent

load_dotenv(base_dir.joinpath('.env'))


class Config:
    DEV = os.getenv('DEV', False)
    DB_REGION_NAME = os.getenv('DB_REGION_NAME')
    DB_ACCESS_KEY_ID = os.getenv('DB_ACCESS_KEY_ID')
    DB_SECRET_ACCESS_KEY = os.getenv('DB_SECRET_ACCESS_KEY')


def initialize_db() -> ServiceResource:
    if Config.DEV:
        dynamodb = boto3.resource('dynamodb',
                                  region_name=Config.DB_REGION_NAME,
                                  aws_access_key_id=Config.DB_ACCESS_KEY_ID,
                                  aws_secret_access_key=Config.DB_SECRET_ACCESS_KEY)
    else:
        dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
    return dynamodb
