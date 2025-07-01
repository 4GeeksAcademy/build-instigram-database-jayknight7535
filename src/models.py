from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Table, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from datetime import date


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Users(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[int] 
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    followers: Mapped[int] = mapped_column(nullable=False)
    following: Mapped[int] = mapped_column(nullable=False)
    post: Mapped[int] = mapped_column(nullable=False)
    profile_pic: Mapped[str] = mapped_column(String())


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "is_active": self.is_active,
            "followers": self.followers,
            "following": self.following,
            "post": self.post,
            "profile_pic": self.profile_pic
            # do not serialize the password, its a security breach
        }
class post(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    post_user: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    liked: Mapped[int] 
    chat_response: Mapped[int] 
    date_posted: Mapped[date] 
    saved: Mapped[int]
    shared_link: Mapped[int]
    hashtags: Mapped[str] = mapped_column(unique=True)


    def serialize(self):
        return {
            "id": self.id,
            "post_user": self.email,
            "liked": self.liked,
            "chat_response": self.chat_response,
            "date_posted": self.date_posted,
            "saved": self.saved,
            "shared_link": self.shared_link,
            "hashtags": self.hashtags
            # do not serialize the password, its a security breach
        }    
class Chat(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_message: Mapped[str]
    user_posted: Mapped[str] = mapped_column(nullable=False)
    like: Mapped[int]
    user_profile_pic:Mapped[str]


    def serialize(self):
        return {
            "id": self.id,
            "chat_message": self.chat_message,
            "user_posted": self.user_posted,
            "like": self.like,
            "user_profile_pic": self.user_profile_pic
            # do not serialize the password, its a security breach
        }
