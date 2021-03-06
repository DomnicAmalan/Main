from sqlalchemy.orm import Session

from ..models import usermodel
from ..schemas import users_schema
from ...helpers import encrypt


def create_user(db: Session, user: users_schema.User):
    user.Password = encrypt.get_password_hash(user.Password)
    db_user = usermodel.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    del db_user.Password
    return db_user

def check_username_exists(db: Session, Username):
    return db.query(usermodel.User).filter(usermodel.User.Username == Username).first()

def check_email_mobile_exists(db: Session, Email, Mobilenumber):
    return db.query(usermodel.User).filter(usermodel.User.Email == Email, usermodel.User.Mobilenumber == Mobilenumber).first()

def login_check(db: Session, Email, Password):
    hashed_password = db.query(usermodel.User).filter(usermodel.User.Email == Email).first()
    if hashed_password:
        return encrypt.verify_password(Password, hashed_password.Password)
    return "No User Found"
