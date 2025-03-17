from fastapi import FastAPI
from app.controllers import user_controller
from app.db.database import engine
from app.models import user

# Crear tablas en la base de datos
user.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MVC")

# Incluir rutas del controlador
app.include_router(user_controller.router, tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a FastAPI MVC"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
