from fastapi import FastAPI
from helpers import TransactionsHelper

app = FastAPI()

transactions_helper = TransactionsHelper('us-east-1', 'transactions')


@app.get("/")
def read_root():
    return {"body": "Hello World!"}


@app.get("/transactions")
def get_all_transactions():
    return transactions_helper.fetch_all()


@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    pass

# TODO : If year_month not provided, take current year and month
app.get("/transactions/month/{year_month}")
def get_months_transactions(year_month: str):
    pass

# TODO : If year not provided, take current year
app.get("/transactions/year/{year}")
def get_years_transactions(year: str):
    pass


app.get("/transactions/category/{category}")
def get_transactions_by_category(category: str):
    pass


app.get("/transactions/category/{category}/month/{year_month}")
def get_transactions_by_category_and_month(category: str, year_month: str):
    pass

