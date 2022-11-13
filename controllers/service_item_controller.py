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

    stmt = db.select(Vehicle).filter_by(id=id)
    vehicle = db.session.scalar(stmt)
    if vehicle:
        vehicle.deleted = True
        vehicle.updated_at = datetime.datetime.now()
        db.session.commit()
        return {'message': f"Vehicle'{vehicle.make}' deleted successfully"}
    else:
        return {'error': f'Vehicle not found with id {id}'}, 404


@service_item_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_vehicle(id):
    stmt = db.select(Vehicle).filter_by(id=id)
    vehicle = db.session.scalar(stmt)
    now = datetime.datetime.now()
    if vehicle:
        vehicle.vin = request.json.get('vin') 
        vehicle.make = request.json.get('make') 
        vehicle.model = request.json.get('model')
        vehicle.year = request.json.get('year')
        vehicle.created_at = now
        vehicle.updated_at = now
        db.session.commit()      
        return VehicleSchema().dump(vehicle)
    else:
        return {'error': f'Owner not found with id {id}'}, 404


@service_item_bp.route('/', methods=['POST'])
# @jwt_required()
def create_vehicle():
    now = datetime.datetime.now()
    vehicle = Vehicle(
        vin = request.json.get('vin'), 
        make = request.json.get('make'), 
        model = request.json.get('model'),
        year = request.json.get('year'),
        created_at = now,
        updated_at = now
    )
    
    db.session.add(vehicle)
    try:
        db.session.commit()
    except IntegrityError:
        return {'error': f'vehicle with {vehicle.vin} already exists'}, 400
  
    return VehicleSchema().dump(vehicle), 201

