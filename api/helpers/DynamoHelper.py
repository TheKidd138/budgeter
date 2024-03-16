import boto3


class DynamoHelper:

    def __init__(self, region, table):
        self.client = boto3.client('dynamodb', region_name=region)
        self.table_name = 'budg-dev-' + table
        print('DynamoHelper instance created.')
        return

    # TODO : Clean up this function
    def fetch_all(self):
        scan_params = {'TableName': self.table_name}
        # print(table_name)
        # print(type(self.client))
        response = self.client.scan(**scan_params)
        # print(response)
        items = response['Items']
        # For Loop Implementation
        # for item in items:
        #     for key, value in item.items():
        #         item[key] = list(value.values())[0]

        # List comprehension of above for loops
        items = [{key: list(value.values())[0]
                  for key, value in item.items()} for item in items]
        # print(items)
        return (items)
