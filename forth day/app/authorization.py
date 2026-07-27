from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "your_secret_key_here"  
ALGORITHM = "HS256"

def create_access_token(user_id: int, name: str, expires_minutes: int = 30):
    """Login successful hone ke baad ye token banega"""
    payload = {
        "sub": str(user_id),        # 'subject' - kis user ke liye hai
        "name": name,
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)  # expiry
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token: str):
    """Har protected request pe ye token verify hoga"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expire ho gaya, dobara login karein")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


