from pydantic import BaseModel
from typing import Optional

# DTO para crear usuario
class UserCreateDTO(BaseModel):
    name: str
    email: str  # Cambiado de EmailStr a str para evitar dependencias extras
    password: str

# DTO para respuesta
class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
