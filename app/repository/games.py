from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource


class Games:
    def __init__(self, db: ServiceResource) -> None:
        self.__db = db

    def get_all(self):
        try:
            table = self.__db.Table('Games')
            response = table.scan()
            return response['Items']
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(e)

    def get_game(self, uid: str):
        try:
            table = self.__db.Table('Games')
            response = table.get_item(Key={'uid': uid})
            return response['Item']
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(e)

    def create_game(self, game: dict):
        try:
            table = self.__db.Table('Games')
            response = table.put_item(Item=game)
            return response
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(e)
