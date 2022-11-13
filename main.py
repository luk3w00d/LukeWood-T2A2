from flask import Flask, send_from_directory
from init import db, ma, bcrypt, jwt
from controllers.service_controller import service_bp
from controllers.owner_controller   import owner_bp
from controllers.vehicle_controller import vehicle_bp
from controllers.service_item_controller import service_item_bp
from controllers.image_controller import image_bp
from cli_command import db_commands

import os

def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401

    @app.route('/images/<name>')
    def download_file(name):
        return send_from_directory(app.config["UPLOAD_FOLDER"], name)

    # @app.errorhandler(KeyError)
    # def KeyError(err):
    #     return {'error': f'The field {err} is required.'}, 400

    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:8080/car_service'
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'images')
    app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(service_bp)
    app.register_blueprint(owner_bp)
    app.register_blueprint(vehicle_bp)
    app.register_blueprint(service_item_bp)
    app.register_blueprint(image_bp)

    return app