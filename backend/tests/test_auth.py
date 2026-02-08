def test_user_register_and_login(client, test_user):
    # Register
    response = client.post(
        "/api/v1/users/register",
        json=test_user
    )

    assert response.status_code in (201, 400)

    # Login
    response = client.post(
        "/api/v1/auth/login",
        json=test_user
    )

    assert response.status_code == 200

    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
