"""Models file."""
from app import db

class Service(db.Model):
    """Class representing a microservice."""

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    host = db.Column(db.String(240))

    def __init__(self, name, host=None):
        self.name = name
        self.host = host if host is not None else self.host_from_name()

    def host_from_name(self):
        return 'http://{}'.format(self.name)

    def to_dict(self):
        return {
            'name': self.name,
            'id': self.pk,
            'host': self.host
        }
