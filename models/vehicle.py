from marshmallow import fields
from init import db, ma


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String)
    make = db.Column(db.String)
    model = db.Column(db.String) 
    year = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)

    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    
    # vehicle = db.relationship('Vehicle', back_populates='Vehicle')


class VehicleSchema(ma.Schema):
    
    

    class Meta:
        fields = ('id', 'vin', 'make', 'model', 'year', 'created_at', 'updated_at', 'deleted')
        ordered = True