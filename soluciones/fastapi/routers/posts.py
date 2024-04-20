from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
from fastapi import APIRouter
from database import get_db

#Enrutador para el manejo de rutas
router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get('/', response_model=List[schemas.GetPost], summary="Obtener todas las notas") #response_model: se obtiene una lista de objetos de la clase Getpost
def test_posts(db: Session = Depends(get_db)): #sesion en la base de datos

    post = db.query(models.Post).all() #Se obtiene una lista de todos los resultados


    return  post # se devuuelve la lista

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreatePost], summary="Crear una nota")
def test_posts_sent(post_post:schemas.CreatePost, db:Session = Depends(get_db)): #toma como parámetro un objeto de la clase Createpost para añadir los campos

    new_post = models.Post(**post_post.dict())
    db.add(new_post)
    db.commit() #confirmar la transacción en la base de datos
    db.refresh(new_post) #asegurarse de que refleje los cambios realizados

    return [new_post]



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,summary="Borrar una nota")
def delete_test_post(id:int, db:Session = Depends(get_db)):

    deleted_post = db.query(models.Post).filter(models.Post.id == id)


    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    deleted_post.delete(synchronize_session=False)
    db.commit()



@router.put('/posts/{id}', response_model=schemas.CreatePost, summary="Editar una nota")
def update_test_post(update_post:schemas.PostBase, id:int, db:Session = Depends(get_db)):

    updated_post =  db.query(models.Post).filter(models.Post.id == id)

    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_post.update(update_post.dict(), synchronize_session=False)
    db.commit()


    return  updated_post.first()


@router.put('/posts/done/{id}', response_model=schemas.CreatePost, summary="Marcar una nota como realizada")
def update_test_post(update_post:schemas.UpdatePost, id:int, db:Session = Depends(get_db)):

    updated_post =  db.query(models.Post).filter(models.Post.id == id)

    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_post.update(update_post.dict(), synchronize_session=False)
    db.commit()


    return  updated_post.first()