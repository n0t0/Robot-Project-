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

response = table.get_item(
    Key={
        # 'username': 'n0t0',
        'username': user,
        'last_name': 'Ivanov'
    }
)
item = response['Item']
print(item)


if user in item.values():
    print('Hi', user.upper(), '!')
    # check database
    # add friends list to dynamodb
    # api token to facebook
    # vault/consul
    # key/value (primary/compose)

else:
    print ('Hi {}. It is nice to meet you! My owner is {}'.format(
        user.title(), owner.upper()))
    print ('Analysing...')    # func needed (Amazon Rekognition)
    print ('Implanting...')  # func needed (Amazon Polly)
    # new_friends.append(user)
    # table.put_item(
    #     Item={
    #         'username': 'Maya',
    #         'first_name': 'Mila',
    #         'last_na/me': 'Yana',
    #         'age': 32,
    #         # 'account_type': 'admin',
    #         'account_type': 'standart_user',
    #     }
    # )
    table.put_item(
        Item={
            'username': user,
            'first_name': 'Goran',
            'last_name': 'Bregovic',
            'age': 32,
            'account_type': 'standart_user',
        }
    )
    print(user, 'Added to database')   # lambda func to DynamoDB
