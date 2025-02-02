from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.routers import contacts
from src.database.db import get_db
from src.services.middlewares import ProcessTimeHeaderMiddleware

app = FastAPI()
app.add_middleware(ProcessTimeHeaderMiddleware)

app.include_router(contacts.routerContacts, prefix='/api')

@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        # Make request
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


@app.get("/")
async def root():
    return {"message": "Navigation page"}

