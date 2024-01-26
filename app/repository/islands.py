from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource


class Islands:
    def __init__(self, db: ServiceResource) -> None:
        self.__db = db

    def get_all(self):
        try:
            table = self.__db.Table('Islands')
            response = table.scan()
            return response['Items']
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(e)

    def get_island(self, seed: int):
        try:
            table = self.__db.Table('Islands')
            response = table.get_item(Key={'seed': seed})
            return response['Item']
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(e)

    def get_random(self):
        try:
            return True  # TODO implement
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(e)
