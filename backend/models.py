from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User_Info(db.Model):
    __tablename__="userinfo"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String, unique=True, nullable=False)
    password=db.Column(db.String, nullable=False)
    first_name=db.Column(db.String, nullable=False)
    last_name=db.Column(db.String, nullable=True)
    dob=db.Column(db.DateTime, nullable=False)      
    address=db.Column(db.String,nullable=False)
    pincode=db.Column(db.Integer, nullable=False)   
    contact=db.Column(db.Integer, nullable=False)
    role=db.Column(db.Integer, nullable=False)
    bookings=db.relationship("Bookings",cascade="all,delete",backref="userinfo",lazy=True)

class Profs(db.Model):
    __tablename__="prof"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String, unique=True, nullable=False)
    password=db.Column(db.String, nullable=False)
    first_name=db.Column(db.String, nullable=False)
    last_name=db.Column(db.String, nullable=True)
    date_joined=db.Column(db.DateTime)
    status=db.Column(db.String,nullable=False,default="pending")
    dob=db.Column(db.DateTime, nullable=False)      
    service_type=db.Column(db.String, nullable=False)   
    address=db.Column(db.String,nullable=False)
    rating=db.Column(db.Integer,default=1)
    pincode=db.Column(db.Integer, nullable=False)   
    role=db.Column(db.Integer,nullable=False)
    contact=db.Column(db.Integer, nullable=False)
    bookings=db.relationship("Bookings",cascade="all,delete",backref="prof",lazy=True)

class Services(db.Model):
    __tablename__="services"
    service_id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    base_price=db.Column(db.Integer, nullable=False)
    desc=db.Column(db.String)
    bookings=db.relationship("Bookings",cascade="all,delete",backref="services",lazy=True)

class Bookings(db.Model):
    booking_id=db.Column(db.Integer,primary_key=True)
    date_of_booking=db.Column(db.DateTime, nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey("userinfo.id"), nullable=False)
    prof_id=db.Column(db.Integer,db.ForeignKey("prof.id"), nullable=False)
    service_id=db.Column(db.Integer,db.ForeignKey("services.service_id"), nullable=False)
    rating=db.Column(db.Integer)
    remarks=db.Column(db.Integer)
    status=db.Column(db.Integer)