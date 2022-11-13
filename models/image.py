from init import db, ma
from marshmallow import fields


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    created_at = db.Column(db.datetime)
    updated_at = db.Column(db.datetime)
    deleted = db.Column(db.Boolean)

    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)


    user = db.relationship('Owner', back_populates='cards')


class ImageSchema(ma.Schema):

    image = fields.List(fields.Nested('ImageSchema'))

    class Meta:
        fields = ('id', 'url', 'created_at', 'updated_at', 'deleted')
        ordered = True