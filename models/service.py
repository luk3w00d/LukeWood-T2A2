from marshmallow import fields
from init import db, ma


class Service(db.Model):
    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    vehicle = db.relationship('Vehicle', back_populates='services')
     


class ServiceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_time', 'end_time', 'created_at', 'updated_at', 'deleted')
        ordered = True