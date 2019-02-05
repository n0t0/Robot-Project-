from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.

user = input('What is your name?\n').lower()


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource(
    'dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Friends')

print("This user is a friend")

response = table.query(
    KeyConditionExpression=Key('username').eq(user)
)

for i in response['Items']:
    print(i['username'], ":", i['last_name'])


# def hello():
#     '''
#     Greet the person.
#     Add to database if BRF made a new friend.
#     '''
#     user = input('What is your name?\n').lower()
#     if user in response:
#         print('Hi', user.upper(), '!')
#         # check database
#         # add friends list to dynamodb
#         # api token to facebook
#         # vault/consul
#         # key/value

#         # mv ln24 def emotion_detect(): function checking for user's state
#         # pass emotion_detect() as an argument to behDecision()
#     else:
#         print ('Hi {}. It is nice to meet you! My owner is {}'.format(
#             user.title(), owner.upper()))
#         print ('Analysing...')    # func needed (Amazon Rekognition)
#         print ('Implanting...')  # func needed (Amazon Polly)
#         new_friends.append(user)
#         print ('Added to database')   # lambda func to DynamoDB
#         print (new_friends)
