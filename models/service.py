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

    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)

    # user = db.relationship('Owner', back_populates='service')
    


class ServiceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_time', 'end_time', 'created_at', 'updated_at', 'deleted')
        ordered = True