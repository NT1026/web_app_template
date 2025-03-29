# Web Application Template

## Frontend

- Framework: Next.js

### Prepared 

- Need Node.js and npm
- Install node packages in `package.json`
```
npm install 
```

### Run Frontend Server (for development)

- Work directory: `/frontend`

- Execute `npm run dev` command to start development frontend server

## Backend

- RESTful API framework: FastAPI
- Web Server framework: Uvicorn
- Database: MySQL
- Database ORM Model: Pydantic + SQLAlchemy

### Prepared

- Install python modules in `requirements.txt`
```
pip install -r requirements.txt
```

- Run MySQL server container (default: 8888 port)
```
docker run --name mysql_database -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=test_database -p 8888:3306 --volume mysql_database:/var/lib/mysql -d mysql:8.1
```

### Run Backend Server

- Work directory: `backend`
- Run `main.py` to start backend server
