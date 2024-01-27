import boto3
from boto3.resources.base import ServiceResource

from app.configuration.config import Config


def initialize_db() -> ServiceResource:
    if Config.DEV:
        dynamodb = boto3.resource('dynamodb',
                                  region_name=Config.DB_REGION_NAME,
                                  aws_access_key_id=Config.DB_ACCESS_KEY_ID,
                                  aws_secret_access_key=Config.DB_SECRET_ACCESS_KEY)
    else:
        dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
    return dynamodb
