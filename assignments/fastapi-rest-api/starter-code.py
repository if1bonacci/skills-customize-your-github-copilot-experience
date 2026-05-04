# FastAPI REST API Starter Code

"""
This starter code provides a basic FastAPI app structure.
Complete the tasks in the assignment README to build out the full API.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add your endpoints and models below
