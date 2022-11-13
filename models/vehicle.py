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

    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    image = db.relationship('Image', cascade='all, delete')
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id') )
    owner = db.relationship('Owner', back_populates='vehicles')
    services = db.relationship('Service', back_populates='vehicle', cascade='all, delete')

class VehicleSchema(ma.Schema):

    vehicle = fields.List(fields.Nested('VehicleSchema'))


    class Meta:
        fields = ('id', 'vin', 'make', 'model', 'year', 'created_at', 'updated_at', 'deleted')
        ordered = True