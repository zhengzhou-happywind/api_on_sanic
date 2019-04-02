from sanic import Sanic

from .view import bp

app = Sanic(__name__)
app.blueprint(bp)
