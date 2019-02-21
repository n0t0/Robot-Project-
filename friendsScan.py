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

response = table.scan()
data = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])

print(data)

for username in data:
    if username == user:
        print ('HI')
    else:
        print ('Not found!')

# if user in data:
#     print('Hi', user.upper(), '!')


# else:
#     print ('Hi {}. It is nice to meet you! My owner is {}'.format(
#         user.title(), owner.upper()))
#     print ('Analysing...')    # func needed (Amazon Rekognition)
#     print ('Implanting...')  # func needed (Amazon Polly)
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
