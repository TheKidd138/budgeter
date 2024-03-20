import datetime

from helpers import TransactionsHelper

helper = TransactionsHelper('us-east-1', 'transactions')

def get_year_month():
    current_datetime = datetime.datetime.now()
    # Extract the year and month components
    current_year = current_datetime.year
    current_month = current_datetime.month
    # Format the year and month as YYYYMM
    year_month = '{:04d}{:02d}'.format(current_year, current_month)
    return year_month

year_month = get_year_month()
print(year_month)
resp = helper.fetch_month(year_month)

# helper.fetch_one('1')

# resp = helper.fetch_all()
# resp = helper.fetch_one('3')
# resp = helper.fetch_month('202403')
# resp = helper.fetch_year('2024')
# resp = helper.fetch_category_by_month('mortgage','202403')
# resp = helper.fetch_category_by_year('mortgage','2024')
print(resp)


