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


response = table.get_item(
    Key={
        'username': 'n0t0',
        'last_name': 'Ivanov'
    }
)
item = response['Item']
print(item)
