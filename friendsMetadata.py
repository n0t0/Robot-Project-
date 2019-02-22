import boto3

# Get the service resource.
dynamodb = boto3.resource(
    'dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Friends')


def get_table_metadata(table):
    """
    Get some metadata about chosen table.
    """
    table = dynamodb.Table('Friends')

    return {
        'num_items': table.item_count,
        'primary_key_name': table.key_schema[0],
        'status': table.table_status,
        'bytes_size': table.table_size_bytes,
        'global_secondary_indices': table.global_secondary_indexes
    }


print (get_table_metadata(table))


def read_table_item(table, pk_name, pk_value):
    """
    Return item read by primary key.
    """
    table = dynamodb.Table(table)
    response = table.get_item(Key={pk_name: pk_value})

    return response


read_table_item(table, 'username', pk_value)
