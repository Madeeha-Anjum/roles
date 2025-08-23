from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.engine import get_db

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    
    return db.query('SELECT * FROM address ORDER BY id DESC').offset(skip).limit(limit).all()