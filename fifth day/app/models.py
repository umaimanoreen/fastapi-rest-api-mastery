from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base
book_student = Table('book_student', Base.metadata,
                     Column('book_id', Integer, ForeignKey('books.id')),
                     Column('student_id', Integer, ForeignKey('students.id')),
                     Column('created_at', DateTime,
                            default=datetime.now(timezone.utc))
                     )


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    students = relationship("Student", back_populates="user")
    books = relationship("Book", back_populates="user")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    user = relationship("User", back_populates="students")
    books = relationship("Book", secondary=book_student,
                         back_populates="students")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    user = relationship("User", back_populates="books")
    students = relationship(
        "Student", secondary=book_student, back_populates="books")


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    subject = Column(String, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
