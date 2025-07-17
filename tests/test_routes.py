from app import app


def test_homepage_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "hello" in response.data.decode("utf-8")
