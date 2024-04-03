import boto3


class BalancesHelper():

    def __init__(self, region, table):
        self.client = boto3.client('dynamodb', region_name=region)
        self.table_name = 'budg-dev-' + table
        print('TransactionHelper instance created.')
        return
    

    def __format_response(self, response: dict):
        # print(response)
        if 'Items' in response:
            # Multiple items to format
            items = response['Items']
            
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
        

    def fetch_all(self):
        scan_params = {'TableName': self.table_name}
        response = self.client.scan(**scan_params)
        # print(response)
        items = self.__format_response(response)
        return(items)