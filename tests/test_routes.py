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


# Test Cookies
def test_set_cookie_get():
    client = app.test_client()
    response = client.get("/setcookie")
    assert response.status_code == 200


def test_set_cookies_set():
    client = app.test_client()
    response = client.post("/setcookie", data={"ID": "30"})
    assert response.status_code == 200
    cookie_header = response.headers.get(
        "Set-Cookie"
    )  # i did that in line response.set_cookie("userID", user_ID)
    assert "userID=30" in cookie_header


def test_get_cookies_after_set_cookie():
    client = app.test_client()
    response = client.post("/setcookie", data={"ID": "30"})
    assert response.status_code == 200

    # check if cookies is saved

    cookie = response.headers.get("Set-Cookie")
    assert "userID=30" in cookie

    # Send GET request and check cookie value
    response = client.get("/getcookie", headers={"Cookie": "userID=30"})
    assert response.status_code == 200
    assert "Welcome 30" in response.data.decode("utf-8")
