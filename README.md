# Budgeter :)

# Quick References

## FastAPI & ASGI Server (Uvicorn)

### FastAPI Docs

    - https://fastapi.tiangolo.com/#installation

### ASGI Server??

    - The Asynchronous Server Gateway Interface is a calling convention for web servers to forward requests to asynchronous-capable Python programming language frameworks, and applications. It is built as a successor to the Web Server Gateway Interface.

### Uvicorn Docs

    - https://www.uvicorn.org/

### Start/Stop/Reload Uvicorn

    - (START) uvicorn main:app
    - (RELOAD) uvicorn main:app --reload
    - (STOP) CTRL + C

## Activate/Deactivate venv

    - source ../venv/budgeter/bin/activate
    - deactivate

## requirements.txt

### Create requirements.txt

    - pip freeze > requirements.txt

### Install from requirements.txt

    - pip install -r requirements.txt
