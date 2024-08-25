# FastAPI auth API with SQLite database

I just put together FastAPI's OAuth2 feature into a small project which uses a SQLite database.

<hr>

#### Install:

1. To run this project on your locally, first clone the repo and enter the folder in your terminal. Now setup a VENV with the command:

```
python -m venv venv
```

2. After that has been created activate the virtual environment by typing in your terminal:

```
venv\Scripts\activate
```

3. Now to install the project dependencies type:

```
pip install -r requirements.txt
```

4. From the root of the project, you'll need to run this command:

```
python app/setup_db.py
```

5. Once that is done, you can run the server with this command:

```
uvicorn app.main:app

```

The server will now start. The first address is the first API endpoint. The second address is the automatically generated interactive doc.

```
http://127.0.0.1:8000/api
http://127.0.0.1:8000/docs
```

<hr>

##### Tools and technologies used:

-   Python
-   FastAPI
