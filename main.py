from database import create_db
from api.v1.endpoints.company import router as company_router
from fastapi import FastAPI

#this will creates tables in database
create_db()

app = FastAPI()
app.include_router(company_router)