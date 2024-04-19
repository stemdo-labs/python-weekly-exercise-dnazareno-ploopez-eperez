from fastapi import FastAPI
from fastapi import FastAPI
from database import engine
import models
# Importar los modelos para que se registren
# Esto es importante para que SQLAlchemy pueda crear las tablas en la base de datos
from models import Post
import psycopg2
from routers import posts


app = FastAPI()

app.include_router(posts.router)

models.Base.metadata.create_all(bind=engine)
