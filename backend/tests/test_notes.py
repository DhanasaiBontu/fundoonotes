def get_token(client, test_user):
    response = client.post(
        "/api/v1/auth/login",
        json=test_user
    )
    return response.json()["access_token"]


def test_create_note_authenticated(client, test_user):
    token = get_token(client, test_user)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = client.post(
        "/api/v1/notes",
        headers=headers,
        json={
            "title": "PyTest Note",
            "description": "Created via pytest"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "PyTest Note"


def test_create_note_unauthorized(client):
    response = client.post(
        "/api/v1/notes",
        json={
            "title": "Fail Note",
            "description": "Should fail"
        }
    )

    assert response.status_code == 401
