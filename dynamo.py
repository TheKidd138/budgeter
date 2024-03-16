import boto3

region = 'us-east-1'

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name=region)

# Specify the table name
table_name = 'budg-dev-transactions'

# Specify the month you want to query
target_month = '202402'  # Example month in format 'YYYY-MM'

# Construct the scan parameters with filtering
scan_params = {
    'TableName': table_name,
    'FilterExpression': 'begins_with(#sortkey, :month)',
    'ExpressionAttributeValues': {
        ':month': {'S': target_month}
    },
    'ExpressionAttributeNames': {
        '#sortkey': 'YearMonth'
    }
}

# Execute the scan operation
response = dynamodb.scan(**scan_params)
print(response)

# Process the response
items = response['Items']
for item in items:
    # Process individual item as needed
    print(item)


print('Here')
