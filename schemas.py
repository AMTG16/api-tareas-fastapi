from pydantic import BaseModel

class TareaBase(BaseModel):
    titulo: str
    descripcion: str | None = None
    completada: bool = False

class TareaCreate(TareaBase):
    pass

class TareaUpdate(TareaBase):
    pass

class Tarea(TareaBase):
    id: int

    class Config:
        orm_mode = True
