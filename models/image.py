


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    created_at = db.Column(db.datetime)
    updated_at = db.Column(db.datetime)
    deleted = db.Column(db.Boolean)

    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)

    user = db.relationship('Owner', back_populates='cards')
    comments = db.relationship('Comment', back_populates='card', cascade='all, delete')


class CardSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['card']))

    class Meta:
        fields = ('id', 'url', 'created_at', 'updated_at', 'deleted')
        ordered = True