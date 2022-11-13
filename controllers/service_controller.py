import datetime
from flask import Blueprint, request
from init import db
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service import Service, ServiceSchema


service_bp = Blueprint('service', __name__, url_prefix='/service')


@service_bp.route('/')
# @jwt_required()
def get_service():
    stmt = db.select(Service).order_by(Service.created_at.desc())
    services = db.session.scalars(stmt)
    return ServiceSchema(many=True).dump(services)


@service_bp.route('/<int:id>/')
def get_one_service(id):
    stmt = db.select(Service).filter_by(id=id)
    service = db.session.scalar(stmt)
    if service:
        return ServiceSchema().dump(service)
    else:
        return {'error': f'Service not found with id {id}'}, 404


@service_bp.route('/<int:id>/', methods=['DELETE'])
# @jwt_required()
def delete_one_service(id):
    # authorize()

    stmt = db.select(Service).filter_by(id=id)
    service = db.session.scalar(stmt)
    if service:
        db.session.delete(service)
        db.session.commit()
        return {'message': f"Service'{service}' deleted successfully"}
    else:
        return {'error': f'Service not found with id {id}'}, 404


@service_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_service(id):
    stmt = db.select(Service).filter_by(id=id)
    service = db.session.scalar(stmt)
    now = datetime.datetime.now()
    if service:
        service.start_time = now 
        service.end_time = datetime 
        service.created_at = now
        service.update_at = datetime
        return ServiceSchema().dump(service)
    else:
        return {'error': f'service not found with id {id}'}, 404


@service_bp.route('/', methods=['POST'])
# @jwt_required()
def create_service():
    now = datetime.datetime.now()
    service = Service(
        start_time = request.json.get('start_time'),
        end_time = request.json.get('end_time'),
        created_at = now,
        updated_at = now
    )
  
    db.session.add(service)
    db.session.commit()
    
    return ServiceSchema().dump(service), 201

