import datetime
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request
from init import db
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.owner import Owner, OwnerSchema




owner_bp = Blueprint('owner', __name__, url_prefix='/owner')


@owner_bp.route('/')
# @jwt_required()
def get_owners():
    stmt = db.select(Owner).order_by(Owner.created_at.desc())
    owners = db.session.scalars(stmt)
    return OwnerSchema(many=True).dump(owners)


@owner_bp.route('/<int:id>/')
def get_one_owner(id):
    stmt = db.select(Owner).filter_by(id=id)
    owner = db.session.scalar(stmt)
    if owner:
        return OwnerSchema().dump(owner)
    else:
        return {'error': f'Owner not found with id {id}'}, 404


@owner_bp.route('/<int:id>/', methods=['DELETE'])
# @jwt_required()
def delete_one_owner(id):
    # authorize()

    stmt = db.select(Owner).filter_by(id=id)
    owner = db.session.scalar(stmt)
    if owner:
        owner.deleted = True
        owner.updated_at = datetime.datetime.now()
        db.session.commit()
        return {'message': f"Owner '{owner.first_name} {owner.last_name}' deleted successfully"}
    else:
        return {'error': f'Owner not found with id {id}'}, 404


@owner_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_owner(id):
    stmt = db.select(Owner).filter_by(id=id)
    owner = db.session.scalar(stmt)
    if owner:
        owner.first_name = request.json.get('first_name') or owner.first_name
        owner.last_name = request.json.get('last_name') or owner.last_name
        owner.email = request.json.get('email') or owner.email
        owner.phone = request.json.get('phone') or owner.phone
        owner.updated_at = datetime.datetime.now()
        db.session.commit()      
        return OwnerSchema().dump(owner)
    else:
        return {'error': f'Owner not found with id {id}'}, 404


@owner_bp.route('/', methods=['POST'])
# @jwt_required()
def create_owner():
    now = datetime.datetime.now()
    owner = Owner(
        first_name = request.json.get('first_name'), 
        last_name = request.json.get('last_name'), 
        email = request.json.get('email'), 
        phone = request.json.get('phone'), 
        updated_at = now,
        created_at = now
    )
    
    db.session.add(owner)
    try:
        db.session.commit()
    except IntegrityError:
        return {'error': f'Owner with email {owner.email} already exists'}, 400
  
    return OwnerSchema().dump(owner), 201

