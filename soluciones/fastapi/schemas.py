from pydantic import BaseModel

#Creación de diferentes clases con diferentes campos dependiendo de lo que se quiera crear/editar/leer

class PostBase(BaseModel):
    content: str
    title: str

    class Config:
        orm_mode = True


class CreatePost(PostBase):
    class Config:
        orm_mode = True


class UpdatePost(BaseModel):
    done: bool

    class Config:
        orm_mode = True

class GetPost(BaseModel):
    done: bool
    content: str
    title: str

    class Config:
        orm_mode = True