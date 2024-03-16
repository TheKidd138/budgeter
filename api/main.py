from typing import Union

from fastapi import FastAPI
from helpers import DynamoHelper

app = FastAPI()

transactions_helper = DynamoHelper('us-east-1', 'transactions')


@app.get("/")
def read_root():
    return {"body": "Hello World!"}


@app.get("/transactions")
def get_all_transactions():
    return transactions_helper.fetch_all()

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
