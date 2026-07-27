from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Generic, TypeVar
from datetime import datetime

T = TypeVar("T")


class pagination(BaseModel, Generic[T]):
    total: int
    page: int
    size: int
    total_pages: int


class UserCreate(BaseModel):
    username: str = Field(max_length=100, min_length=3)
    password: str = Field(max_length=100, min_length=6)
    email: EmailStr = Field(..., max_length=100)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TeacherCreate(BaseModel):
    name: str = Field(max_length=100, min_length=3)
    email: EmailStr = Field(..., max_length=100)
    subject: str = Field(max_length=100, min_length=3)


class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class StudentCreate(BaseModel):
    name: str = Field(max_length=100, min_length=3)
    age: int = Field(..., gt=0)
    user_id: int


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class BookCreate(BaseModel):
    title: str = Field(max_length=100, min_length=3)
    author: str = Field(max_length=100, min_length=3)


class assignmentCreate(BaseModel):
    book_id: int
    student_id: int
