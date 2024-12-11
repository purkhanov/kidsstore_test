from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.products.routes import router as product_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors.ORIGINS,
    allow_credentials = True,
    allow_methods = settings.cors.ALLOW_METHODS,
    allow_headers = settings.cors.ALLOW_HEADERS,
)


app.include_router(product_router)
