from app.models import db
from app.models.base import SoftDeletionModel


class EventOrgaModel(SoftDeletionModel):
    """Event sub topic object table"""

    __tablename__ = 'events_orga'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    starts_at = db.Column(db.DateTime(timezone=True))
    payment_currency = db.Column(db.String, nullable=False)

    def __init__(self,
                 name=None):

        self.name = name

    def __repr__(self):
        return '<EventOrgaModel %r>' % self.name

    def __str__(self):
        return self.__repr__()

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {'id': self.id, 'name': self.name}

# from app.models import db
# from app.models.base import SoftDeletionModel
#
#
# class EventOrga(SoftDeletionModel):
#     """Event sub topic object table"""
#
#     __tablename__ = 'event_sub_topics_test'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String, nullable=False)
#
#     def __init__(self,
#                  name=None):
#
#         self.name = name
#
#     def __repr__(self):
#         return '<EventOrga %r>' % self.name
#
#     def __str__(self):
#         return self.__repr__()
#
#     @property
#     def serialize(self):
#         """Return object data in easily serializable format"""
#         return {'id': self.id, 'name': self.name}
