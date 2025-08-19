from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, Base, engine

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Tareas")

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.post("/tareas/", response_model=schemas.Tarea)
def crear_tarea_endpoint(tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    return crud.crear_tarea(db, tarea)

@app.get("/tareas/", response_model=list[schemas.Tarea])
def leer_tareas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tareas(db, skip=skip, limit=limit)

@app.get("/tareas/{tarea_id}", response_model=schemas.Tarea)
def leer_tarea(tarea_id: int, db: Session = Depends(get_db)):
    db_tarea = crud.get_tarea(db, tarea_id)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea

@app.put("/tareas/{tarea_id}", response_model=schemas.Tarea)
def actualizar_tarea_endpoint(tarea_id: int, tarea: schemas.TareaUpdate, db: Session = Depends(get_db)):
    db_tarea = crud.actualizar_tarea(db, tarea_id, tarea)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea

@app.delete("/tareas/{tarea_id}", response_model=schemas.Tarea)
def eliminar_tarea_endpoint(tarea_id: int, db: Session = Depends(get_db)):
    db_tarea = crud.eliminar_tarea(db, tarea_id)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea
