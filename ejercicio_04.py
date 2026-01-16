import sqlite3
from contextlib import contextmanager
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional, List


app = FastAPI(
    title="Cuarta API",
    description="Esta es mi cuarta API para practicar FastAPI con SQLite",
    version="1.0.0",
)

DATABASE_NAME = "estudiantes.db"

