from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.resume import router as resume_router
from app.routers.analyze import router as analyze_router
from app.routers.analysis import router as analysis_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="AI Career Intelligence Platform",
    description="AI-powered Resume & Career Intelligence API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health_router)
app.include_router(resume_router)

app.include_router(analyze_router)

app.include_router(analysis_router)



@app.get("/")
def root():
    return {
        "status": "running",
        "service": "AI Career Intelligence Platform",
        "version": "1.0.0"
    }


