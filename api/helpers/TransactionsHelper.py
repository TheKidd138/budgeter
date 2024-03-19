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
        items = response['Items']
        # For Loop Implementation
        # for i,item in enumerate(items):
        #     trans_dict = {}
        #     for key, value in item.items():
        #         trans_dict[key] = list(value.values())[0]
        #     print(trans_dict)
        #     items[i] = trans_dict

        # List comprehension of above for loops
        if not items:
            print('API call returned no values')
            return(None)
        items = [{key: list(value.values())[0]
                    for key, value in item.items()} for item in items]
        # print(items)
        return(items)

    
    def fetch_all(self):
        scan_params = {'TableName': self.table_name}
        response = self.client.scan(**scan_params)
        # print(response)
        items = self.__format_response(response)
        return(items)
        

    def fetch_one(self, transaction_id: str):
        get_params = {
            'TableName': self.table_name,
            'Key':{'transaction_id':{'S': '2'}}
        }
        response = self.client.get_item(**get_params)
        print(response)
        items = self.__format_response(response)
        # If no item found, return NONE to avoid error.
        if not items:
            return(None)
        return(items[0])

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

