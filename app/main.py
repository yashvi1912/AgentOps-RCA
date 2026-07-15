from fastapi import FastAPI

from app.database import Base, engine
from app.routes.logs import router as logs_router
from app.routes.analyze import router as analyze_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AgentOps",
    description="AI-powered observability platform",
    version="0.1"
)

# Register routers
app.include_router(logs_router)
app.include_router(analyze_router)

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "AgentOps"
    }
