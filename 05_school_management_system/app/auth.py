from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
teacher_password = pwd_context.hash("teacher123")
pwd_context.verify("teacher123", teacher_password)
