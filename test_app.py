import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Zoek een boek!" in response.data.decode("utf-8")


def test_find_book_success(client):
    response = client.post("/zoek", data={"isbn": "PI0488208"})
    assert response.status_code == 200
    assert "Zoek een boek!" in response.data.decode("utf-8")
    assert "Boek Gevonden!" in response.data.decode("utf-8")
    assert "&#39;Eis ijs!&#39; zei zij" in response.data.decode("utf-8")


def test_book_not_found(client):
    response = client.post("/zoek", data={"isbn": "0000000000000"})
    assert response.status_code == 200
    assert "niet gevonden" in response.data.decode("utf-8")
    assert "Boek Gevonden!" not in response.data.decode("utf-8")


def test_invalid_isbn_short(client):
    response = client.post("/zoek", data={"isbn": "123"})
    assert response.status_code == 200
    assert "niet gevonden" in response.data.decode("utf-8")
    assert "Boek Gevonden!" not in response.data.decode("utf-8")


def test_invalid_isbn_long(client):
    response = client.post("/zoek", data={"isbn": "1234567890123456"})
    assert response.status_code == 200
    assert "niet gevonden" in response.data.decode("utf-8")
    assert "Boek Gevonden!" not in response.data.decode("utf-8")


def test_empty_isbn(client):
    response = client.post("/zoek", data={"isbn": ""})
    assert response.status_code == 200
    assert "niet gevonden" in response.data.decode("utf-8")
    assert "Boek Gevonden!" not in response.data.decode("utf-8")
