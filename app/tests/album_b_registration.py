from app.tests import client



route_url = "/album_registration"

# Tesing if users with valid credentials
# can register successfully.

def test_album_registration_pass():
    response = client.post(
        route_url,
        json={
            "artist_id": 1,
            "album_name": "Album"
        }
    )
    assert response.status_code == 201
    assert response.json() == 'Successful Album Registration'


def test_album_registration_fail():
    response = client.post(
        route_url,
        json={
              "artist_id": 0,
            "album_name": "Album"
        }
    )
    assert response.status_code == 401
    assert response.json()['detail'] == 'Invalid Album Registration'