from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/users")
def list_users(request: Request, db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return templates.TemplateResponse("users.html", {
        "request": request,
        "users": users
    })

@router.get("/users/new")
def new_user_form(request: Request):
    return templates.TemplateResponse("user_form.html", {
        "request": request
    })

@router.post("/users")
def create_user(
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    crud.create_user(db, schemas.UserCreate(name=name, email=email))
    return RedirectResponse(url="/users", status_code=303)
