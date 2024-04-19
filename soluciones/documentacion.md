# CRUD de la API y conexión a la base de datos
## Configuración del entorno:
Para llevar a cabo el proyecto y preparar el entorno es necesario instalar: - Python - Postgress - psycopg2: psycopg2 es un adaptador de base de datos PostgreSQL para Python. Permite conectarnos a una base de datos PostgreSQL desde nuestra aplicación de python.

Crear un entorno virtual: 

``` 
python -m venv fastapi-env
```

Activación del entorno virtual

``` 
fastapi-env\Scripts\activate.bat
```

Instalación de FastAPI para documentar la API y Uvicorn para ejecutarla 
```
pip install fastapi
pip install uvicorn
``` 

Finalmente se utiliza uvicorn para ejecutar la aplicación: 
```
uvicorn main:app --reload
```
(main es el archivo principal y app el nombre de la aplicación)

## Configuración y creación de tablas para la Base de Datos
Se crea un archivo database.py con la configuración de la base de datos, incluyendo la URL de conexión y la función para obtener la sesión de la base de datos.

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1598@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Creación del archivo models.py para definir la tabla de la base de datos

```
from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    done = Column(Boolean, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
```
## API CRUD
Implementación de las operaciones CRUD en un archivo posts.py
Definición los modelos Pydantic en un archivo schemas.py para la validación y serialización de datos.
Incluir el enrutador de la API en el archivo main.py del proyecto:

```
app.include_router(posts_router)
```