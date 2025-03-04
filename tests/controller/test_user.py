def test_get(client, session):
    response = client.get("/users")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
