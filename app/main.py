from fastapi import FastAPI
from mangum import Mangum

from app.schemas import Person

app = FastAPI(docs_url="/")


@app.post("/people", status_code=200)
async def person_skills(person: Person):
    return person


@app.get("/people", status_code=200)
def person_skills_get():
    fake_data = {
        "name": "John Doe",
        "age": 30,
        "skills": [
            {
                "skill_name": "Python",
                "skill_level": 10
            }
        ]
    }
    return fake_data


# For Aws lambda to work
handler = Mangum(app=app)
