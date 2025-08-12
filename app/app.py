from fastapi import FastAPI
import os
import asyncpg

app = FastAPI()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/appdb"

@app.on_event("startup")
async def startup():
    app.state.connection = await asyncpg.connect(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown():
    await app.state.connection.close()

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a mi aplicación Free Tier!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/db-check")
async def db_check():
    try:
        result = await app.state.connection.fetch("SELECT 1")
        return {"db_status": "ok", "result": result}
    except Exception as e:
        return {"db_status": "error", "detail": str(e)}