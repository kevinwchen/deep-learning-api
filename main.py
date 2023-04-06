from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator
import tasks

app = FastAPI()

# Route 1:
# Test if working
# { "message": "Hello World!"}

@app.get("/")
def get_root():
    return {"message": "Hello World!"}

# Route 2: /translate
# Take in a translation request, store it the database
# Return a transaction id

# Route 3: /results
# Take in a translation id
# Return the translated text

