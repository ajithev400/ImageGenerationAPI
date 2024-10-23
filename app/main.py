from fastapi import FastAPI
from app.endpoints import image_generation

app = FastAPI(
    title="Replicate Image Generation API",
    description="API for generating images using Replicate's AI models.",
    version="1.0.0"
)

app.include_router(image_generation.router, prefix="/api/v1/images")
