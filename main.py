from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator
from models import TranslationModel
import tasks

app = FastAPI()

langueages = ["English", "French", "German", "Romanian"]

class Translation(BaseModel):
    text: str
    base_lang: str
    final_lang: str

    @validator('base_lang', 'final_lang')
    def valid_lang(cls, lang):
        if lang not in langueages:
            raise ValueError("Invalid language")
        return lang

# Route 1:
# Test if working
# { "message": "Hello World!"}

@app.get("/")
def get_root():
    return {"message": "Hello World!"}

# Route 2: /translate
# Take in a translation request, store it the database
# Return a transaction id
@app.post("/translate")
def post_translation(t: Translation, background_tasks: BackgroundTasks):
    # Store the translation
    # Run the translation in the background
    t_id = tasks.store_translation(t)
    background_tasks.add_task(tasks.run_translation, t_id)
    return {"task_id": t_id}


# Route 3: /results
# Take in a translation id
# Return the translated text
@app.get("/results")
def get_translation(t_id: int):
    model = TranslationModel.get_by_id(t_id)

    translation = model.translation
    if translation is None:
        translation = "Processing, check back later"

    return translation

