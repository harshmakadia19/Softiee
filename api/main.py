import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexroute
from .models import model_loader
from .dependencies.config import conf


app = FastAPI(
    title="Softiee OROS: Online Restaurant Ordering System API",
    description="Full API documentation for the Online Restaurant Ordering System.",
    version="1.0.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexroute.load_routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)