from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_skill():
    response_auth = client.get(f"/people")
    assert response_auth.status_code == 200


def test_add_skill():
    response_auth = client.post("/people", json={
        "name": "John Doe",
        "age": 30,
        "skills": [
            {
                "skill_name": "Python",
                "skill_level": 10
            }
        ]
    })
    assert response_auth.status_code == 200
    assert response_auth.json() == {
        "name": "John Doe",
        "age": 30,
        "skills": [
            {
                "skill_name": "Python",
                "skill_level": 10
            }
        ]
    }
