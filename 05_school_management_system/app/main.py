from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, engine
import app.models as models
import app.schemas as schemas
from typing import List
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/teachers", status_code=201)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = models.Teacher(
        name=teacher.name,
        email=teacher.email,
        subject=teacher.subject
    )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


@app.get("/teachers", response_model=List[schemas.TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(models.Teacher).all()
    return teachers


if get_teachers is None:
    raise HTTPException(status_code=404, details="teacher not found")


@app.put("teachers/{teachers_id}")
def update_teacher(teachers_id: int,
                   teachers: schemas.TeacherCreate, db: Session = Depends(get_db)):

    db_teacher = db.query(models.Teacher).filter(
        models.Teacher.id == teachers_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db_teacher.name = teachers.name
    db_teacher.subject = teachers.subject
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(
        models.Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete(db_teacher)
    db.commit()
    return {"message": "Teacher deleted successfully"}
