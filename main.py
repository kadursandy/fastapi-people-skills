from fastapi import FastAPI, status
from schemas import Person

app = FastAPI(docs_url="/")


@app.post("/people/", status_code=200)
async def person_skills(person: Person):
    return person
