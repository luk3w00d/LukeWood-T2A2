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
def delete_one_card(id):
    # authorize()

    stmt = db.select(Service).filter_by(id=id)
    service = db.session.scalar(stmt)
    if service:
        db.session.delete(service)
        db.session.commit()
        return {'message': f"Service'{service}' deleted successfully"}
    else:
        return {'error': f'Service not found with id {id}'}, 404


# @service_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
# @jwt_required()
# def update_one_card(id):
#     stmt = db.select(Card).filter_by(id=id)
#     card = db.session.scalar(stmt)
#     if card:
#         card.title = request.json.get('title') or card.title
#         card.description = request.json.get('description') or card.description
#         card.status = request.json.get('status') or card.status
#         card.priority = request.json.get('priority') or card.priority
#         db.session.commit()      
#         return CardSchema().dump(card)
#     else:
#         return {'error': f'Card not found with id {id}'}, 404


# @service_bp.route('/', methods=['POST'])
# @jwt_required()
# def create_card():
#     # Create a new Card model instance
#     card = Card(
#         title = request.json['title'],
#         description = request.json['description'],
#         date = date.today(),
#         status = request.json['status'],
#         priority = request.json['priority'],
#         user_id = get_jwt_identity()
#     )
#     # Add and commit card to DB
#     db.session.add(card)
#     db.session.commit()
#     # Respond to client
#     return CardSchema().dump(card), 201


# @service_bp.route('/<int:card_id>/comments', methods=['POST'])
# @jwt_required()
# def create_comment(card_id):
#     stmt = db.select(Card).filter_by(id=card_id)
#     card = db.session.scalar(stmt)
#     if card:
#         comment = Comment(
#             message = request.json['message'],
#             user_id = get_jwt_identity(),
#             card = card,
#             date = date.today()
#         )
#         db.session.add(comment)
#         db.session.commit()
#         return CommentSchema().dump(comment), 201
#     else:
#         return {'error': f'Card not found with id {id}'}, 404
