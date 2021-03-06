from datetime import datetime
from app import db,long_manager
from flask_login import UserMixin


@long_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))
    

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique = True,nullable = False)
    email = db.Column(db.String(130),unique = True,nullable = False)
    image_file = db.Column(db.String(30),nullable = False,default='default.jpg')
    password = db.Column(db.String(60), nullable = False)
    pitch = db.relationship('pitch',backref='author',lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Pitch(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable = False)
    date_posted =db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
    content = db.Column(db.Text,nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"