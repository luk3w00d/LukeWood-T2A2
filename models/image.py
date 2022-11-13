from init import db, ma
from marshmallow import fields


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)



class ImageSchema(ma.Schema):

    image = fields.List(fields.Nested('ImageSchema'))

    class Meta:
        fields = ('id', 'url', 'created_at', 'updated_at', 'deleted')
        ordered = True