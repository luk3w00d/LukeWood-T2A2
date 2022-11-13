import datetime
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request
from init import db
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.service_item import Service_item, Service_itemSchema




service_item_bp = Blueprint('service_item', __name__, url_prefix='/service_item')


@service_item_bp.route('/')
# @jwt_required()
def get_service_items():
    stmt = db.select(Service_item).order_by(Service_item.created_at.desc())
    service_items = db.session.scalars(stmt)
    return Service_itemSchema(many=True).dump(service_items)


@service_item_bp.route('/<int:id>/')
def get_one_Service_item(id):
    stmt = db.select(Service_item).filter_by(id=id)
    service_item = db.session.scalar(stmt)
    if service_item:
        return Service_itemSchema().dump(service_item)
    else:
        return {'error': f'Service item not found with id {id}'}, 404


@service_item_bp.route('/<int:id>/', methods=['DELETE'])
# @jwt_required()
def delete_one_service_item(id):
    # authorize()

    stmt = db.select(Service_item).filter_by(id=id)
    service_item = db.session.scalar(stmt)
    if service_item:
        service_item.deleted = True
        service_item.updated_at = datetime.datetime.now()
        db.session.commit()
        return {'message': f"Service item'{service_item}' deleted successfully"}
    else:
        return {'error': f'Service item not found with id {id}'}, 404


@service_item_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_service_item(id):
    stmt = db.select(Service_item).filter_by(id=id)
    service_item = db.session.scalar(stmt)
    now = datetime.datetime.now()
    if service_item:
        service_item.item_type = request.json.get('item_type') 
        service_item.cost = request.json.get('cost') 
        service_item.qty = request.json.get('qty')
        service_item.notes = request.json.get('notes')
        service_item.created_at = now
        service_item.updated_at = now
        db.session.commit()      
        return Service_itemSchema().dump(service_item)
    else:
        return {'error': f'Service item not found with id {id}'}, 404


@service_item_bp.route('/', methods=['POST'])
# @jwt_required()
def create_service_item():
    now = datetime.datetime.now()
    service_item = Service_item(
        item_type = request.json.get('item_type'), 
        cost = request.json.get('cost'), 
        qty = request.json.get('qty'),
        notes = request.json.get('notes'),
        created_at = now,
        updated_at = now
    )
    
    db.session.add(service_item)
    try:
        db.session.commit()
    except IntegrityError:
        return {'error': f'Service item with {service_item} already exists'}, 400
  
    return Service_itemSchema().dump(service_item), 201

