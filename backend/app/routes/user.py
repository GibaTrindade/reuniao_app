from fastapi import APIRouter, Depends, HTTPException, security
from typing import List
from sqlalchemy import orm
from..schemas.index import User, UserCreate, ChangePassword
from ..services import get_db, get_user_by_email, create_user, \
    get_all_users, get_user_by_id, update_user, create_token, authenticate_user, \
    get_current_user

user = APIRouter()

@user.get("/users", response_model=List[User], tags=["user"])
async def read_data(db: orm.Session=Depends(get_db)):
    db_users = get_all_users(db=db)
    return db_users


@user.get("/users/{user_id}", response_model=User, tags=["user"])
def read_user(user_id: int, db: orm.Session = Depends(get_db)):

    db_user = get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user


@user.post("/users", tags=["user"])
async def create_user_route(
    user: UserCreate, db: orm.Session = Depends(get_db)
):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="woops the email is in use"
        )
    #create a user
    user_created = await create_user(db=db, user=user)
    print("validou")
    return await create_token(user=user_created)

@user.post("/token", tags=["user"])
async def generate_token(
        form_data: security.OAuth2PasswordRequestForm = Depends(),
        db: orm.Session = Depends(get_db)):

    user_token = authenticate_user(email=form_data.username, password=form_data.password, db=db)

    if not user_token:
        raise HTTPException(status_code=401, detail="Credenciais inválidas!")

    return await create_token(user=user_token)

@user.get("/current_user/me", response_model=User, tags=["user"])
async def get_user(user: User = Depends(get_current_user)):
    return user

@user.put("/admin/users/{user_id}", response_model=User, tags=["user"])
def update_post(
    user_id: int,
    user: UserCreate,
    db: orm.Session = Depends(get_db),
):

    return update_user(db=db, user=user, user_id=user_id)

@user.put("/users", response_model=User, tags=["user"])
def update_post(
    user: UserCreate,
    db: orm.Session = Depends(get_db),
    cur_user: User = Depends(get_current_user)
):
    user_id = cur_user.id
    return update_user(db=db, user=user, user_id=user_id)
