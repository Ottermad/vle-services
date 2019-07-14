"""Views file."""
from flask import Blueprint, request, jsonify
from internal.helper import (
    json_from_request,
    check_keys,
    check_values_not_blank
)

from app import db
from .models import Service

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/register", methods=("POST",))
def register_service():
    """Endpoint to register a service if it does not exist yet."""
    # Get JSON data from request
    json_obj = json_from_request(request)

    # Check keys
    keys = ['name', 'k8s_name']
    check_keys(keys, json_obj)
    check_values_not_blank(keys, json_obj)

    # Check if service exists
    service = Service.query.filter_by(name=json_obj['name']).first()
    if service is None:
        service = Service(name=json_obj['name'], k8s_name=json_obj['k8s_name'])
        db.session.add(service)
        db.session.commit()

    return jsonify({'success': True}), 201

@main_blueprint.route("/services")
def list_services():
    """Endpoint to list all services."""
    services = Service.query.all()
    services_list = [s.to_dict() for s in services]
    return jsonify({'success': True, 'services': services_list})
