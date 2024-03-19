
from helpers import TransactionsHelper

helper = TransactionsHelper('us-east-1', 'transactions')

# helper.fetch_one('1')

# resp = helper.fetch_month('202403')
# resp = helper.fetch_year('2024')
# resp = helper.fetch_category_by_month('mortgage','202403')
resp = helper.fetch_category_by_year('mortgage','2024')
print(resp)


