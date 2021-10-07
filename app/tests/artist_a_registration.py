from app.tests import client



route_url = "/artist_registration"

# Tesing if users with valid credentials
# can register successfully.

def test_artist_registration_pass():
    response = client.post(
        route_url,
        json={
            "name": "Lil BuX",
            "gendre": "HipHop",
            "country": "SA",
        }
    )
    assert response.status_code == 201
    assert response.json() == 'Successful Artist Registration'


def test_artist_registration_fail():
    response = client.post(
        route_url,
        json={
             "name": "Lil BuX",
             "gendre": "HipHop",
             "country": "SA",
        }
    )
    assert response.status_code == 401
    assert response.json()['detail'] == 'Invalid Artist Registration'