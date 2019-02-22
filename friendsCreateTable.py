import boto3

# Get the service resource.
dynamodb = boto3.resource(
    'dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Friends',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'   # Partition Key
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'  # Sort Key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='Friends')

# Print out some data about the table.
print(table.item_count)
