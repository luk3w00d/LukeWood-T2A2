from init import db, ma
from marshmallow import fields

class Owner(db.Model):
    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String)                      
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)



class OwnerSchema(ma.Schema):
    services = fields.List(fields.Nested('ServiceSchema'))

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at', 'deleted')
        ordered = True