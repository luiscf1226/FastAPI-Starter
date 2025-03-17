from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.dtos.user_dto import UserCreateDTO, UserResponseDTO
from app.repositories.user_repository import UserRepository

router = APIRouter()

@router.get("/users/", response_model=List[UserResponseDTO])
def get_users(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    users = repository.get_all()
    return users

@router.get("/users/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    user = repository.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/users/", response_model=UserResponseDTO)
def create_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    db_user = repository.get_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return repository.create(user)
