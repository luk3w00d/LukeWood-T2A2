import datetime
import os
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request
from init import db
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.image import Image, ImageSchema




image_bp = Blueprint('image', __name__, url_prefix='/image')




@image_bp.route('/<int:id>/')
def get_one_image(id):
    stmt = db.select(Image).filter_by(id=id)
    image = db.session.scalar(stmt)
    if image:
        return ImageSchema().dump(image)
    else:
        return {'error': f'Image not found with id {id}'}, 404


@image_bp.route('/<int:id>/', methods=['DELETE'])
# @jwt_required()
def delete_one_image(id):
    # authorize()
    stmt = db.select(Image).filter_by(id=id)
    image = db.session.scalar(stmt)
    if image:
        image.deleted = True
        image.updated_at = datetime.datetime.now()
        db.session.commit()
        return {'message': f"Image '{image.url} ' deleted successfully"}
    else:
        return {'error': f'Image not found with id {id}'}, 404


@image_bp.route('/', methods=['POST'])
# @jwt_required()
def create_image():

    file = request.files['photo']
    filename = secure_filename(file.filename)
    file.save('images/' + filename)
    
    now = datetime.datetime.now()
    image = Image(
        url = 'images/' + filename, 
        updated_at = now,
        created_at = now

    )
    
    db.session.add(image)
    try:
        db.session.commit()
    except IntegrityError:
        return {'error': f'Image url {image.url} already exists'}, 400
  
    return ImageSchema().dump(image), 201

