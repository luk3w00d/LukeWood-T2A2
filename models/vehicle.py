from marshmallow import fields
from init import db, ma


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String)
    make = db.Column(db.String)
    model = db.Column(db.String) 
    year = db.Column(db.Integer)
    created_at = db.Column(db.datetime)
    updated_at = db.Column(db.datetime)
    deleted = db.Column(db.Boolean)

    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    owner = db.relationship('Owner', back_populates='Service')
    


class VehicleSchema(ma.Schema):
    owner = fields.Nested('OwnerSchema', only=['first_name', 'email'])
    

    class Meta:
        fields = ('id', 'vin', 'make', 'model', 'year', 'created_at', 'updated_at', 'deleted')
        ordered = True