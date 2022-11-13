from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.service import Service
from models.service_item import Service_item
from models.vehicle import Vehicle
from models.owner import Owner



db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    owners = [
        Owner(
            first_name='Fred',
            last_name='Wild',
            email='143faker@gmail.com',
            phone='1233455',
            # password=bcrypt.generate_password_hash('potato').decode('utf-8'),
            # is_admin=True
        ),
        Owner(
            first_name='Bill',
            last_name='Frank',
            email='redred@gmail.com',
            phone='677756',
            # password=bcrypt.generate_password_hash('stars').decode('utf-8')
        )
    ]

    db.session.add_all(owners)
    db.session.commit()

    vehicle = [
        Vehicle(
            vin='23423ds123123fdsssa',
            make='volkswagon',
            model='passat',
            year='2008',

        ),
        Vehicle(
            vin='4564krk45k-0242',
            make='valiant',
            model='ve',
            year ='1969'
        )
    ]

    db.session.add_all(vehicle)
    db.session.commit()

    service = [
        Service(
            start_time = date.today(),
            end_time = date.today(),
        ),
        Service(
            start_time = date.today(),
            end_time = date.today(),
        )

    ]

    db.session.add_all(service)
    db.session.commit()

    service_item = [
        Service_item(
            item_type='filter',
            cost='344',
            notes='needs potato'
           

        ),
        Service_item(
            item_type='oil',
            cost='343444',
            notes='needs ddd'
        )
    ]

    db.session.add_all(vehicle)
    db.session.commit()



    print('Tables seeded')
