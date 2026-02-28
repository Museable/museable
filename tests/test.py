import requests
from aiohttp.log import access_logger

print("Creating user...")
user = requests.post(
    "http://localhost:5000/api/auth/register",
    json = {
        "email": "user@test.com",

        "username": "user",
        "password": "password"
    }
)

if not user.ok:
    if user.status_code == 409:
        print("User already exists")
    else:
        raise Exception("User creation failed")

print("Logging in as user...")
user = requests.post(
    "http://localhost:5000/api/auth/login",
    json = {
        "email": "user@test.com",
        "username": "user",
        "password": "password"
    }
)

if not user.ok:
    raise Exception("User login failed")

access_token = user.json()["access_token"]
refresh_token = user.json()["refresh_token"]

print(f"Logged in as user with access token {access_token}")

print("Getting user infos...")

infos = requests.get(
    "http://localhost:5000/api/auth/get_infos",
headers={"Authorization": f"Bearer {access_token}"}
)

if not infos.ok:
    raise Exception("User getting infos failed")

print("User infos :")
print(infos.json())

print("Promoting the user as publisher...")

request = requests.post(
    "http://localhost:5000/api/auth/promote",
headers={"Authorization": f"Bearer {access_token}"}
)

if not request.ok:
    raise Exception("User promotion failed")

infos = requests.get(
    "http://localhost:5000/api/auth/get_infos",
headers={"Authorization": f"Bearer {access_token}"}
)

print("User infos :")
print(infos.json())

print("Publishing a song...")
request = requests.post(
    "http://localhost:5000/api/tracks/create",
    files={"file": open("tests/sample.mp3", "rb")},
    headers={"Authorization": f"Bearer {access_token}"},
    data={
        "title": "Sample title",
        "artist": "Sample artist",
        "album": "Sample album",
        "cover": "Sample cover",
    }
)

if not request.ok:
    print(request.text)
    raise Exception("Song creation failed")

print("Song creation successful")

print("Getting all tracks...")

request = requests.get("http://localhost:5000/api/tracks")

if not request.ok:
    raise Exception("Tracks getting failed")

print(request.json())