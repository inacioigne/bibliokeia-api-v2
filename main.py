from typing import Union
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#from datetime import datetime, timedelta
from jose import JWTError, jwt
from src.db.init_db import initializeDatabase
from fastapi.middleware.cors import CORSMiddleware
from src.routes.users import login
from src.routes.users import users
from src.routes.cataloguing import items
from src.routes.cataloguing import exemplar
from src.routes.cataloguing import authority
from src.routes.search import acervo
from src.routes.circulation import loan, devolution
from security import SECRET_KEY, JWT_ALGORITHM



initializeDatabase()

app = FastAPI(
    title="BiblioKeia",
    description="Backend API for BiblioKeia",
    contact={
        "name": "Inácio Oliveira",
        "url": "https://github.com/inacioigne",
        "email": "dp@x-force.example.com",
    }
)

origins = [
    "http://localhost:3000",
    'http://127.0.0.1:3000',
    "http://172.21.214.56:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE'],
    allow_headers=["*"],
)


app.include_router(login.router, tags=['Login'])
app.include_router(users.router, prefix='/user', tags=['Users'])
app.include_router(items.router, prefix='/cataloguing/item', tags=['Cataloguing Item'])
app.include_router(exemplar.router, prefix='/cataloguing/exemplar', tags=['Cataloguing Exemplar'])
app.include_router(authority.router, prefix='/cataloguing/authority', tags=['Cataloguing Authority'])
app.include_router(acervo.router, prefix='/acervo', tags=['Acervo'])
app.include_router(loan.router, prefix='/circulation', tags=['Circulation'])
app.include_router(devolution.router, prefix='/circulation', tags=['Circulation'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)