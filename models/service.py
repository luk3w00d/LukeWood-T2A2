


class Service(db.Model):
    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.datetime)
    end_time = db.Column(db.datetime)
    
    created_at = db.Column(db.datetime)
    updated_at = db.Column(db.datetime)
    deleted = db.Column(db.Boolean)

    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)

    user = db.relationship('Owner', back_populates='service')
    comments = db.relationship('Comment', back_populates='service', cascade='all, delete')


class CardSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['card']))

    class Meta:
        fields = ('id', 'start_time', 'end_time', 'created_at', 'updated_at', 'deleted')
        ordered = True