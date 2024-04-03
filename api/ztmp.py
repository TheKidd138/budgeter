import datetime

from helpers import TransactionsHelper

helper = TransactionsHelper('us-east-1', 'transactions')

trans = {
    'amount': {'N':'50'},
    'category': {'S':'Personal'},
    'year_month': {'S':'202404'}
}
# helper.create_transaction(trans)
trans2 = {
    'transaction_id': {'S':'4b59da65-2fe8-4fd0-b827-e116900bf3ff'},
    'amount': {'N':'100'},
    'category': {'S':'Personal'},
    'year_month': {'S':'202404'}
}
# helper.update_transaction(trans2)

helper.delete_transaction('4b59da65-2fe8-4fd0-b827-e116900bf3ff')

# helper.fetch_one('1')

# resp = helper.fetch_all()
# resp = helper.fetch_one('3')
# resp = helper.fetch_month('202403')
# resp = helper.fetch_year('2024')
# resp = helper.fetch_category_by_month('mortgage','202403')
# resp = helper.fetch_category_by_year('mortgage','2024')
# print(resp)


