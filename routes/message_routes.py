from flask import Blueprint
from controllers.message_controller import index, create, read, update, delete, reply, answered

message_bp = Blueprint('message_bp', __name__)
message_bp.route('/', methods=['GET'])(index)
message_bp.route('/answered', methods=['GET'])(answered)
message_bp.route('/', methods=['POST'])(create)
message_bp.route('/<int:id>', methods=['GET'])(read)
message_bp.route('/<int:id>', methods=['PUT', 'PATCH'])(update)
message_bp.route('/resposta/<int:id>', methods=['PATCH'])(reply)
message_bp.route('/<int:id>', methods=['DELETE'])(delete)
