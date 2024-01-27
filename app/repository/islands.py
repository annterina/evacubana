from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource

from app.domain.models.island import Island


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

    def create_island(self, island: dict):
        try:
            table = self.__db.Table('Islands')
            response = table.put_item(Item=island)
            return response
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(e)

    def update_island(self, island: dict):
        table = self.__db.Table('Islands')
        response = table.update_item(
            Key={'seed': island.get('seed')},
            UpdateExpression="""
                set
                    notes=:notes,
                    top_scores=:top_scores
            """,
            ExpressionAttributeValues={
                ':notes': island.get('notes'),
                ':top_scores': island.get('top_scores')
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
