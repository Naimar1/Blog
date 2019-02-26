from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# class Movie:
#     '''
#     Movie class to define Movie Objects
#     '''

#     def __init__(self,id,title,overview,poster,vote_average,vote_count):
#         self.id =id
#         self.title = title
#         self.overview = overview
#         self.poster = "https://image.tmdb.org/t/p/w500/" + poster
#         self.vote_average = vote_average
#         self.vote_count = vote_count



# class Review(db.Model):
#     __tablename__ = 'reviews'

#     id = db.Column(db.Integer,primary_key = True)
#     movie_id = db.Column(db.Integer)
#     movie_title = db.Column(db.String)
#     image_path = db.Column(db.String)
#     movie_review = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     users = db.relationship('User',backref = 'role',lazy="dynamic")

#     all_reviews = []

#     def __init__(self,movie_id,title,imageurl,review):
#         self.movie_id = movie_id
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review


#     def save_review(self):
#         db.session.add(self)
#         db.session.commit()

#         Review.all_reviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()

#     @classmethod
#     def get_reviews(cls,id):
#         reviews = Review.query.filter_by(movie_id=id).all()
#         return reviews

#         response = []

#         for review in cls.all_reviews:
#             if review.movie_id == id:
#                 response.append(review)

#         return response


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    users = db.relationship('User',backref = 'role',lazy="dynamic") 
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    pass_secure = db.Column(db.String(255))

    # reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255))
     
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255))
     

    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))


    def __repr__(self):
         return f'User {self.name}'