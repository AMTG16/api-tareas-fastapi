from sqlalchemy.orm import Session
import models, schemas

def get_tareas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tarea).offset(skip).limit(limit).all()

def get_tarea(db: Session, tarea_id: int):
    return db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

def crear_tarea(db: Session, tarea: schemas.TareaCreate):
    db_tarea = models.Tarea(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def actualizar_tarea(db: Session, tarea_id: int, tarea: schemas.TareaUpdate):
    db_tarea = get_tarea(db, tarea_id)
    if db_tarea:
        for key, value in tarea.dict().items():
            setattr(db_tarea, key, value)
        db.commit()
        db.refresh(db_tarea)
    return db_tarea

def eliminar_tarea(db: Session, tarea_id: int):
    db_tarea = get_tarea(db, tarea_id)
    if db_tarea:
        db.delete(db_tarea)
        db.commit()
    return db_tarea
