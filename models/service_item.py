from marshmallow import fields
from init import db, ma


class Service_item(db.Model):
    __tablename__ = 'service_item'

    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String)
    cost = db.Column(db.Integer)
    qty = db.Column(db.Integer) 
    notes = db.Column(db.String)
    created_at = db.Column(db.datetime)
    updated_at = db.Column(db.datetime)
    deleted = db.Column(db.Boolean)

    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    
   
    


class Service_itemSchema(ma.Schema):
    
    

    class Meta:
        fields = ('id', 'item_type', 'cost', 'qty', 'notes', 'created_at', 'updated_at', 'deleted')
        ordered = True