import jwt
from datetime import datetime, timedelta
from flask import current_app

from app import db, bcrypt
from app.models import User


def register_user(username, email, password):

    existing_email = User.query.filter_by(email=email).first()

    if existing_email:
        return {"message": "Email already exists"}, 409

    existing_username = User.query.filter_by(username=username).first()

    if existing_username:
        return {"message": "Username already exists"}, 409

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "User registered successfully"}, 201

def login_user(email, password):

    user = User.query.filter_by(email=email).first()

    if not user:
        return {"message": "Invalid email or password"}, 401

    if not bcrypt.check_password_hash(user.password, password):
        return {"message": "Invalid email or password"}, 401

    payload = {
        "user_id": user.id,
        "email": user.email,
        "exp": datetime.utcnow() + timedelta(
            minutes=current_app.config["JWT_EXPIRATION"]
        )
    }

    token = jwt.encode(
        payload,
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return {
        "message": "Login successful",
        "token": token
    }, 200