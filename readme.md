# Todo API
This project is a Todo App developed using the FastAPI framework. Its purpose is to serve as a simple API backend, which can be integrated with a mobile app or any other frontend application hosted by the user. The API includes an embedded SQLite database for data storage.

This API provides basic CRUD operations and includes auto-generated documentation accessible through Swagger or Redoc.

To start use command below:
```
docker run -d --name todo-con -p 8000:8000 natthaphonarceci/todoapi:latest
```
Then, access it via http://localhost:8000 or http://localhost:8000/docs for swagger WEB UI and http://localhost:8000/redoc for redoc WEB UI in a browser.

You can mount db data (SQLite) by using command below:
```
docker run --rm -d --name todo-con -p 8000:8000 -v /path/to/store:/code/db-data natthaphonarceci/todoapi:latest
```
EX.
```
docker run --rm -d --name todo-con -p 8000:8000 -v ./db-data:/code/db-data natthaphonarceci/todoapi:latest
```