<img width="1028" height="292" alt="Frame 3(1)" src="https://github.com/user-attachments/assets/97b4f758-2860-4eb5-990a-5f427dc0490b" />

# API Documentation

## Authentification

- `/api/auth/register` [POST]

  Create a new account on the database

  **Example request**
  ```json
  {
    "username": "Museable",
    "email": "Museable@example.com",
    "password": "ILoveMuseable"
  }
  ```

  **Example response**
  ```json
  {
    "message": "User created"
  }
  ```

---

- `/api/auth/login` [POST]

  Get an access token and a refresh token with the user's username and password

  **Example request**
  ```json
  {
    "email": "Museable@example.com",
    "password": "ILoveMuseable"
  }
  ```

  **Example response**
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI[...]",
    "refresh_token": "eyJhbGciOiJIUzI[...]"
  }
  ```


---

- `/api/auth/refresh` [POST]

  Get an new access token from a refresh token

  **Example response**
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI[...]"
  }
  ```


---

- `/api/auth/get_infos` [GET]

  Get the user infos with the current token

  **Example response**
  ```json
  {
    "username": "Museable",
    "email": "Museable@example.com",
    "role": "listener"
  }
  ```

# Tracks

- `/api/tracks` [GET]

  Return all the songs of the database

  **Example response**

  *All tracks of the database*

# Testing

- `/api/test/public` [GET]

  This request works like a ping

  **Example response**
  ```
  Hello
  ```


---

- `/api/test/logged` [GET]

  This request works only if you have a token

  **Example response**
  ```
  Hello
  ```


---

- `/api/test/publisher` [GET]

  This request works only if you have a publisher token

  **Example response**
  ```
  Hello
  ```