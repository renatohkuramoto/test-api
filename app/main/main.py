from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.main.config import (apply_routes_config, custom_openapi,
                             exception_config, hidden_schema_config)
from library.infra.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Api Example',
    description='Serviço de exemplo',
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.middleware('http')

apply_routes_config(app)
exception_config(app)
custom_openapi(app)
hidden_schema_config()
