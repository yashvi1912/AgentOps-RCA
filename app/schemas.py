from pydantic import BaseModel

class LogCreate(BaseModel):
    service: str
    level: str
    message: str


class LogResponse(LogCreate):
    id: int

    class Config:
        from_attributes = True