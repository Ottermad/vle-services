"""Models file."""
from app import db

class Service(db.Model):
    """Class representing a microservice."""

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    host = db.Column(db.String(240))
    k8s_name = db.Column(db.String(120), unique=True)

    def __init__(self, name, k8s_name, host=None):
        self.name = name
        self.k8s_name = k8s_name
        self.host = host if host is not None else self.host_from_name()

    def host_from_name(self):
        return 'http://{}'.format(self.name)

    def to_dict(self):
        return {
            'name': self.name,
            'k8s_name': self.k8s_name,
            'id': self.pk,
            'host': self.host
        }
