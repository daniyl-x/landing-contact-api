from flask import Blueprint


api = Blueprint("browser", __name__)


@api.get("/")
def index():
    return {"is_alive": True}
