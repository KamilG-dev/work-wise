from datetime import datetime
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from core.database import db

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(db.String(64), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(db.String(128), nullable=False)

    display_name: Mapped[str] = mapped_column(db.String(64))
    profile_pic: Mapped[int] = mapped_column(db.Integer, nullable=True)

    freelancer: Mapped["Freelancer"] = relationship(back_populates='user')
    offers: Mapped[List["Offer"]] = relationship(back_populates='author')
    images: Mapped[List["Image"]] = relationship(back_populates='user')
    
    def profile_image_url(self):
        image_url = '/image'
        if self.profile_pic:
            image_url = 'image/'+Image.query.filter_by(id=self.profile_pic).first().id
        return image_url

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'display_name': self.display_name,
            'profile_image_url': self.profile_image_url()
        }

class Freelancer(db.Model):
    __tablename__ = 'freelancers'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    user: Mapped[User] = relationship(back_populates='freelancer')

    description: Mapped[str] = mapped_column(db.Text, nullable=False)
    skills: Mapped[str] = mapped_column(db.Text, nullable=False)

    submissions: Mapped[List["Submission"]] = relationship(back_populates='freelancer')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'display_name': self.user.display_name,
            'description': self.description,
            'skills': self.skills,
            'profile_pic': self.user.profile_image_url()
        }

class Offer(db.Model):
    __tablename__ = 'offers'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(db.String(64), nullable=False)
    description: Mapped[str] = mapped_column(db.Text, nullable=False)
    price: Mapped[float] = mapped_column(nullable=True)

    author_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    author: Mapped[User] = relationship(back_populates='offers')

    submissions: Mapped[List["Submission"]] = relationship(back_populates='offer')

    posted_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'posted_at': self.posted_at.isoformat(),
            'price': self.price,
            'author': self.author.to_dict(),
            'submissions': [
                submission.to_dict() for submission in self.submissions
            ]
        }

class Submission(db.Model):
    __tablename__ = 'submissions'

    id: Mapped[int] = mapped_column(primary_key=True)
    freelancer_id: Mapped[int] = mapped_column(db.ForeignKey('freelancers.id'), nullable=False)
    freelancer: Mapped[Freelancer] = relationship(back_populates='submissions')

    offer_id: Mapped[int] = mapped_column(db.ForeignKey('offers.id'), nullable=False)
    offer: Mapped[Offer] = relationship(back_populates='submissions')

    description: Mapped[str] = mapped_column(db.Text, nullable=False)
    price: Mapped[float] = mapped_column(nullable=True)

    posted_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    def to_dict(self):
        return {
            'id': self.id,
            'freelancer': self.freelancer.to_dict(),
            'offer_id': self.offer.id,
            'description': self.description,
            'price': self.price,
            'posted_at': self.posted_at.isoformat()
        }
    
class Image(db.Model):
    __tablename__ = 'images'

    id: Mapped[int] = mapped_column(primary_key=True)
    path: Mapped[str] = mapped_column(db.String(256), nullable=False)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    user: Mapped[User] = relationship(back_populates='images')

    def image_url(self):
        return f'/image/{self.id}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'url': self.image_url()
        }