import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Zoek een Boek" in response.data

def test_find_book_success(client):
    response = client.post('/zoek', data={'isbn': '9789023482329'})
    assert response.status_code == 200
    assert b"Zoek een Boek" in response.data
    assert b"Boek Gevonden!" in response.data
    assert b"De Cirkel" in response.data

def test_book_not_found(client):
    response = client.post('/zoek', data={'isbn': '0000000000000'})
    assert response.status_code == 200
    assert b"niet gevonden" in response.data
    assert b"Boek Gevonden!" not in response.data

def test_invalid_isbn_length_short(client):
    response = client.post('/zoek', data={'isbn': '123'})
    assert response.status_code == 200
    assert b"Ongeldig ISBN" in response.data
    assert b"Boek Gevonden!" not in response.data

def test_invalid_isbn_length_long(client):
    response = client.post('/zoek', data={'isbn': '1234567890123456'})
    assert response.status_code == 200
    assert b"Ongeldig ISBN" in response.data
    assert b"Boek Gevonden!" not in response.data
