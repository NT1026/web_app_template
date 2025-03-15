# Web Application Template

## Frontend
(TODO)

## Backend

### Requirements

- RESTful API framework: FastAPI
- Web Server framework: Uvicorn
- Database: MySQL
- Database ORM Model: Pydantic + SQLAlchemy

### Run Database by Docker

1. Pull MySQL image
```
docker pull mysql:8.1
```

2. Run container
```
docker run --name mysql_database -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=test_database -p 8888:3306 --volume mysql_database:/var/lib/mysql -d mysql:8.1
```

### Start Server
1. Change directory to `backend` (necessary)

2. Run `main.py` to start uvicorn server
```
python main.py
```
