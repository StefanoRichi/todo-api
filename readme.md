# Setup Project
- สร้างไฟล์ .env
```
POSTGRES_HOST=localhost
DB_CONTAINER_NAME=todo_con_db
POSTGRES_DB=todo_db
POSTGRES_USER=todouser
POSTGRES_PASSWORD=1234
```

# init 
- ทำการ init alembic เพื่อสร้างไฟล์ config ในการสร้าง Table
```
 alembic init alembic
```
- Generate Script ที่จะใช้ในการสร้าง Table หรือ Migrate
```
 alembic revision --autogenerate
```
- ทำการ Migrate Table หรือสร้่างขึ้นมาด้วยคำสั่ง
```
 alembic upgrade head
```