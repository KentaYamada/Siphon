from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.user import User
from app.model.mapper.user_mapper import UserMapper


bp = Blueprint('user', __name__, url_prefix='/api/users')


@bp.route('/', methods=['GET'])
def index():
    res = ResponseBody()
    users = User.find_by('')
    res.set_success_response(200, users)
    return res


@bp.route('/', methods=['POST'])
def add():
    res = ResponseBody()

    if request.json is None:
        res.set_fail_response(400)
        return res

    user = User(None, **request.json)

    if not user.is_valid():
        res.set_fail_response(400, user.validation_errors)
        return res

    mapper = UserMapper()
    saved = mapper.add(user)

    if saved:
        res.set_success_response(201)
    else:
        res.set_fail_response(409)
    return res


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    res = ResponseBody()
    user = User(id, **request.json)

    if not user.is_valid():
        res.set_fail_response(400)
        return res

    mapper = UserMapper()
    saved = mapper.edit(user)

    if saved:
        res.set_success_response(200, message='更新しました')
    else:
        res.set_fail_response(409)
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    res = ResponseBody()
    mapper = UserMapper()
    deleted = mapper.delete(id)

    if deleted:
        res.set_success_response(204)
    else:
        res.set_success_response(404)
    return res


@bp.route('/authoricate', methods=['POST'])
def authoricate():
    res = ResponseBody()

    if request.json is None:
        res.set_fail_response(400, message='空のリクエストデータです')
        return res

    mapper = UserMapper()
    can_login = mapper.authoricate(**request.json)

    if can_login:
        res.set_success_response(200, message='認証成功')
    else:
        res.set_fail_response(401, message='認証失敗')
    return res
