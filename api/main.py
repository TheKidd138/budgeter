import datetime

from fastapi import FastAPI
from helpers import TransactionsHelper

app = FastAPI()

transactions_helper = TransactionsHelper('us-east-1', 'transactions')


def get_year_month():
    current_datetime = datetime.datetime.now()
    # Extract the year and month components
    current_year = current_datetime.year
    current_month = current_datetime.month
    # Format the year and month as YYYYMM
    year_month = '{:04d}{:02d}'.format(current_year, current_month)
    return year_month


def get_year():
    current_datetime = datetime.datetime.now()
    # Extract the year component
    current_year = current_datetime.year
    # Format the year and month as YYYY
    year = '{:04d}'.format(current_year)
    return year


@app.get("/")
def read_root():
    return {"body": "Hello World!"}


@app.get("/transactions")
def get_all_transactions():
    return transactions_helper.fetch_all()


@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    return transactions_helper.fetch_one(transaction_id)


@app.get("/transactions/month/")
async def get_current_months_transactions():
    year_month = get_year_month()
    print(year_month)
    return transactions_helper.fetch_month(year_month)


@app.get("/transactions/month/{year_month}")
def get_months_transactions(year_month: str):
    return transactions_helper.fetch_month(year_month)


@app.get("/transactions/year/")
def get_current_years_transactions():
    year = get_year()
    return transactions_helper.fetch_year(year)


@app.get("/transactions/year/{year}")
def get_years_transactions(year: str):
    return transactions_helper.fetch_year(year)


@app.get("/transactions/category/{category}/month/")
def get_transactions_by_category_and_current_month(category: str):
    year_month = get_year_month()
    return transactions_helper.fetch_category_by_month(category, year_month)


@app.get("/transactions/category/{category}/month/{year_month}")
def get_transactions_by_category_and_month(category: str, year_month: str):
    return transactions_helper.fetch_category_by_month(category, year_month)


@app.get("/transactions/category/{category}/year/")
def get_transactions_by_category_and_current_year(category: str):
    year = get_year()
    return transactions_helper.fetch_category_by_month(year)


@app.get("/transactions/category/{category}/year/{year}")
def get_transactions_by_category_and_year(category: str, year: str):
    return transactions_helper.fetch_category_by_month(category, year)