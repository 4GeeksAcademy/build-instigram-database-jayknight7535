from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from datetime import date


class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

Users_to_Posts= Table(
    "Users_to_Posts",
    Base.metadata,
    Column("Users_id", ForeignKey("Users.id")),
    Column("Posts_id", ForeignKey("Posts.id"))
)

Users_to_Chats= Table(
    "Users_to_Posts",
    Base.metadata,
    Column("Users_id", ForeignKey("Users.id")),
    Column("Chats_id", ForeignKey("Chats.id"))
)

Chats_to_Posts= Table(
    "Users_to_Posts",
    Base.metadata,
    Column("Chats_id", ForeignKey("Chats.id")),
    Column("Posts_id", ForeignKey("Posts.id"))
)



class Users(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[int] 
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    followers: Mapped[int] = mapped_column(nullable=False)
    following: Mapped[int] = mapped_column(nullable=False)
    post:  Mapped[list["Posts"]] = relationship(back_populate="Post",secondary= Users_to_Posts,)
    post_id:Mapped[int] = mapped_column(ForeignKey("post.id"))
    profile_pic: Mapped[str] = mapped_column(String())
    chats: Mapped[list["Chats"]] = relationship(back_populate="Chats",secondary=Users_to_Chats,)
    chats_id:Mapped[int] = mapped_column(ForeignKey("chats.id"))
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
            "profile_pic": self.profile_pic,
            "chats": self.chats
            # do not serialize the password, its a security breach
        }
    
class Posts(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user:  Mapped[list["Users"]] = relationship(back_populate="Users",secondary=Users_to_Posts,)
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))
    liked: Mapped[int] 
    chat:  Mapped[list["Chats"]] = relationship(back_populate="Chats",secondary=Chats_to_Posts,)
    chat_id:Mapped[int] = mapped_column(ForeignKey("chat.id"))
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
    
class Chats(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_message: Mapped[str]
    user:  Mapped[list["Users"]] = relationship(back_populate="Users",secondary=Users_to_Chats,)
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))
    like: Mapped[int]
    user_profile_pic:Mapped[str]
    posts: Mapped[list["Posts"]] = relationship(back_populate="Posts",secondary=Chats_to_Posts,)
    posts_id:Mapped[int] = mapped_column(ForeignKey("posts.id"))


    def serialize(self):
        return {
            "id": self.id,
            "chat_message": self.chat_message,
            "user_posted": self.user_posted,
            "like": self.like,
            "user_profile_pic": self.user_profile_pic
            # do not serialize the password, its a security breach
        }
