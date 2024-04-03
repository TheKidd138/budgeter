import uuid

import boto3


class TransactionsHelper:

    def __init__(self, region, table):
        self.client = boto3.client('dynamodb', region_name=region)
        self.table_name = 'budg-dev-' + table
        self.year_month_index = 'year_month-index'
        self.category_index = 'category-index'
        print('TransactionHelper instance created.')
        return
    

    def __format_response(self, response: dict):
        # print(response)
        if 'Items' in response:
            # Multiple items to format
            items = response['Items']

            # List comprehension of above for loops
            if not items:
                print('API call returned no values.')
                return(None)
            items = [{key: list(value.values())[0]
                        for key, value in item.items()} for item in items]
            # print(items)
            return(items)
        else:
            # One item to format
            item = response['Item']
            if not item:
                print('API call returned no value.')
                return(None)
            item = [{key: list(value.values())[0]} for key, value in item.items()]
            # print(item)
            return(item)
        

    def __validate_transaction(self, transaction: dict):
        valid_keys = ['transaction_id','amount','category','year_month']
        transaction_keys = transaction.keys()
        return set(valid_keys) == set(transaction_keys)

    
    def fetch_all(self):
        scan_params = {'TableName': self.table_name}
        response = self.client.scan(**scan_params)
        # print(response)
        items = self.__format_response(response)
        return(items)
        

    def fetch_one(self, transaction_id: str):
        get_params = {
            'TableName': self.table_name,
            'Key':{'transaction_id':{'S': transaction_id}}
        }
        response = self.client.get_item(**get_params)
        # print(response)
        item = self.__format_response(response)
        # If no item found, return NONE to avoid error.
        if not item:
            return(None)
        return(item)


    def fetch_month(self, year_month: str):
        query_params = {
            'TableName': self.table_name,
            'IndexName': self.year_month_index,
            'KeyConditionExpression': 'year_month = :year_month',
            'ExpressionAttributeValues': {
                ':year_month': {'S': year_month}
            }
        }
        response = self.client.query(**query_params)
        items = self.__format_response(response)
        return(items)


    def fetch_year(self, year: str):
        # Can not use begins_with() in query() function
        # query_params = {
        #     'TableName': self.table_name,
        #     'IndexName': self.year_month_index,
        #     'KeyConditionExpression': 'begins_with(year_month, :year)',
        #     'ExpressionAttributeValues': {
        #         ':year': {'S': year}
        #     }
        # }
        # response = self.client.query(**query_params)
        # items = self.__format_response(response)
        # return(items)

        # Create list of months based on year
        months_list = [year + '{:02d}'.format(month) for month in range(1, 13)]
        # Call fetch_month() for each month
        items_lists = [self.fetch_month(month) for month in months_list]
        # Flatten the list of lists into one list of values
        items = [item for sublist in items_lists if sublist for item in sublist]
        return(items)
    

    def fetch_category_by_month(self, category: str, year_month: str):
        query_params = {
            'TableName': self.table_name,
            'IndexName': self.category_index,
            'KeyConditionExpression': 'category = :category AND year_month = :year_month',
            'ExpressionAttributeValues': {
                ':category': {'S': category},
                ':year_month': {'S': year_month}
            }
        }
        response = self.client.query(**query_params)
        items = self.__format_response(response)
        return(items)


    def fetch_category_by_year(self, category: str, year: str):
        # Create list of months based on year
        months_list = [year + '{:02d}'.format(month) for month in range(1, 13)]
        # Call fetch_category_by_month() for each month
        items_lists = [self.fetch_category_by_month(category,month) for month in months_list]
        # Flatten the list of lists into one list of values
        items = [item for sublist in items_lists if sublist for item in sublist]
        return(items)


    def create_transaction(self, transaction: dict):
        transaction['transaction_id'] = {'S': str(uuid.uuid4())}
        if self.__validate_transaction(transaction):
            resp = self.client.put_item(TableName=self.table_name,Item=transaction)
            if resp.get('ResponseMetadata',{'HTTPStatusCode': None}).get('HTTPStatusCode', None) == 200:
                return(True)
            else:
                print('Issue putting item.')
                print(resp)
                return(False)
        else:
            print('Invalid Transaction.')


    def update_transaction(self,transaction: dict):
        if self.__validate_transaction(transaction):
            resp = self.client.put_item(TableName=self.table_name,Item=transaction)
            if resp.get('ResponseMetadata',{'HTTPStatusCode': None}).get('HTTPStatusCode', None) == 200:
                return(True)
            else:
                print('Issue putting item.')
                print(resp)
                return(False)
        else:
            print('Invalid Transaction.')


    def delete_transaction(self, transaction_id: str):
        delete_key = {'transaction_id': {'S':transaction_id}}
        resp = self.client.delete_item(TableName=self.table_name,Key=delete_key)
        if resp.get('ResponseMetadata',{'HTTPStatusCode': None}).get('HTTPStatusCode', None) == 200:
            return(True)
        else:
            print('Issue deleting item.')
            print(resp)
            return(False)