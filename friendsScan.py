import boto3

# Get the service resource.
dynamodb = boto3.resource(
    'dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('Friends')


owner = 'Ivo'
user = input('What is your username?\n').lower()
# last_name = input('What is your last_name?\n').lower()

table = dynamodb.Table('Friends')

response = table.scan()
data = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])

print(data)

# if user in data:
#     print('Hi', user.upper(), '!')


# else:
#     print ('Hi {}. It is nice to meet you! My owner is {}'.format(
#         user.title(), owner.upper()))
#     print ('Analysing...')    # func needed (Amazon Rekognition)
#     print ('Implanting...')  # func needed (Amazon Polly)
#     # new_friends.append(user)
#     # table.put_item(
#     #     Item={
#     #         'username': 'Maya',
#     #         'first_name': 'Mila',
#     #         'last_na/me': 'Yana',
#     #         'age': 32,
#     #         # 'account_type': 'admin',
#     #         'account_type': 'standart_user',
#     #     }
#     # )
#     table.put_item(
#         Item={
#             'username': user,
#             'first_name': 'Goran',
#             'last_name': 'Bregovic',
#             'age': 32,
#             'account_type': 'standart_user',
#         }
#     )
#     print(user, 'Added to database')   # lambda func to DynamoDB
