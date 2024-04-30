from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional, List
import models.moranguinho_models
from create_db import engine, SessionLocal
from sqlalchemy.orm import Session
from core.configs import settings
from api.v1.api import api_router
from . import crud, models, schemas

app= FastAPI(title="API de moranguinho com Xampp")
app.include_router(api_router,prefix=settings.API_V1_STR)
models.moranguinho_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# db_dependecy = Annotated[Session, Depends(get_db)]



if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level="info", reload=True)