from boto3.dynamodb.conditions import Attr
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
            print(f'Error getting islands, {e}')

    def get_all_playable(self):
        try:
            table = self.__db.Table('Islands')
            response = table.scan(FilterExpression=Attr('playable').eq(True))
            return response['Items']
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(f'Error getting islands, {e}')

    def get_seeds(self):
        try:
            table = self.__db.Table('Islands')
            response = table.scan(ProjectionExpression='seed',
                                  FilterExpression=Attr('playable').eq(True))
            return response['Items']
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(f'Error getting seeds, {e}')

    def get_island(self, seed: int):
        try:
            table = self.__db.Table('Islands')
            response = table.get_item(Key={'seed': seed})
            return response['Item']
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(f'Error getting island, {e}')

    def create_island(self, island: dict):
        try:
            table = self.__db.Table('Islands')
            response = table.put_item(Item=island)
            return response
        except ClientError as e:
            print(e.response['Error']['Message'])
        except Exception as e:
            print(f'Error creating island, {e}')

    def update_island(self, island: dict):
        table = self.__db.Table('Islands')
        response = table.update_item(
            Key={'seed': island.get('seed')},
            UpdateExpression="""
                set
                    notes=:notes,
                    top_scores=:top_scores,
                    playable=:playable
            """,
            ExpressionAttributeValues={
                ':notes': island.get('notes'),
                ':top_scores': island.get('top_scores'),
                ':playable': island.get('playable')
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
