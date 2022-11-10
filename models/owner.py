from init import db, ma
from marshmallow import fields

class Owner(db.Model):
    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String)                      
    created_at = db.Column(db.datetime)
    updated_at = db.Column(db.datetime)
    deleted = db.Column(db.boolean)

    owner = db.relationship('Owner', back_populates='owner', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='owner', cascade='all, delete')


# class OwnerSchema(ma.Schema):
#     cards = fields.List(fields.Nested('CardSchema', exclude=['user']))
#     comments = fields.List(fields.Nested('CommentSchema', exclude=['user']))

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at', 'comments')
