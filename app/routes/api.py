from flask import Blueprint


api = Blueprint("browser", __name__)


@api.get("/healthcheck")
def healthcheck():
    return {"is_alive": True}
