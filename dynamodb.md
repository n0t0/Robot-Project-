aws dynamodb list-tables --endpoint-url http://localhost:8000


#### Create Table

aws dynamodb create-table \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --endpoint-url http://localhost:8000

#### Populate a Table

aws dynamodb put-item \
    --table-name Music \
    --item '{ \
        "Artist": {"S": "Acme Band"}, \
        "SongTitle": {"S": "Happy Day"}, \
        "AlbumTitle": {"S": "Songs About Life"} }' \
    --return-consumed-capacity TOTAL \
    --endpoint-url http://localhost:8000