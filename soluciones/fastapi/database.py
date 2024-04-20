from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://equipo:docker@db/ejerciciofinal'
#192.168.1.10
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Crea una sesión en la base de datos cada vez que se hace una petición, capturando las excepciones si es neceario
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()