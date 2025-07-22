from app import app


def test_homepage_get():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_string_var():
    client = app.test_client()
    response = client.get("/Jan")
    assert response.status_code == 200
    assert "Jan" in response.data.decode("utf-8")


def test_admin_page():
    client = app.test_client()
    response = client.get("/admin")
    assert response.status_code == 200
    assert "admin" in response.data.decode("utf-8")


def test_int_var():
    client = app.test_client()
    response = client.get("/blog/24")
    assert response.status_code == 200


def test_float_var():
    client = app.test_client()
    response = client.get("/rev/3.4")
    assert response.status_code == 200
