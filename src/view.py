from sanic import Blueprint
from sanic.response import json

bp = Blueprint('api', url_prefix='/api')


@bp.get('/')
async def api_status(request):
    args = request.args
    print(args)
    res = {
        'msg': 'OK',
    }
    return json(res)
