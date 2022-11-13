import datetime
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request
from init import db
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.vehicle import Vehicle, VehicleSchema




vehicle_bp = Blueprint('vehicle', __name__, url_prefix='/vehicle')


@vehicle_bp.route('/')
# @jwt_required()
def get_vehicles():
    stmt = db.select(Vehicle).order_by(Vehicle.created_at.desc())
    vehicles = db.session.scalars(stmt)
    return VehicleSchema(many=True).dump(vehicles)


@vehicle_bp.route('/<int:id>/')
def get_one_vehicle(id):
    stmt = db.select(Vehicle).filter_by(id=id)
    vehicle = db.session.scalar(stmt)
    if vehicle:
        return VehicleSchema().dump(vehicle)
    else:
        return {'error': f'Vehicle not found with id {id}'}, 404


@vehicle_bp.route('/<int:id>/', methods=['DELETE'])
# @jwt_required()
def delete_one_vehicle(id):
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


@vehicle_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
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
        vehicle.image_id = request.json.get('image_id')
        vehicle.created_at = now
        vehicle.updated_at = now
        db.session.commit()      
        return VehicleSchema().dump(vehicle)
    else:
        return {'error': f'Vehicle not found with id {id}'}, 404


@vehicle_bp.route('/', methods=['POST'])
# @jwt_required()
def create_vehicle():
    now = datetime.datetime.now()
    vehicle = Vehicle(
        vin = request.json.get('vin'), 
        make = request.json.get('make'), 
        model = request.json.get('model'),
        year = request.json.get('year'),
        image_id = request.json.get('image_id'),
        created_at = now,
        updated_at = now
    )
    
    db.session.add(vehicle)
    try:
        db.session.commit()
    except IntegrityError:
        return {'error': f'vehicle with {vehicle.vin} already exists'}, 400
  
    return VehicleSchema().dump(vehicle), 201

