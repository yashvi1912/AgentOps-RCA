from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Log
from app.schemas import LogCreate

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_log(
    log: LogCreate,
    db: Session = Depends(get_db)
):
    new_log = Log(
        service=log.service,
        level=log.level,
        message=log.message
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log


@router.get("/")
def get_logs(
    db: Session = Depends(get_db)
):
    return db.query(Log).all()