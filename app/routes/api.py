import os
from flask import Blueprint, request, current_app

from app.services import (
        ValidationError, validate_data, make_response, write_csv_header,
        write_csv_row
        )


api = Blueprint("api", __name__)


@api.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@api.post("/post")
def post():
    CSV_FIELDS = current_app.config["CSV_FIELDS"]
    OUTPUT_PATH = current_app.config["OUTPUT_PATH"]

    try:
        csv_data = validate_data(request.get_json(), CSV_FIELDS)
    except ValidationError as err:
        return make_response("error", err.message, err.status_code)

    status_code = 200
    if not os.path.exists(OUTPUT_PATH):
        write_csv_header(OUTPUT_PATH, CSV_FIELDS)
        status_code = 201
    write_csv_row(OUTPUT_PATH, csv_data, CSV_FIELDS)

    return make_response(
            "success",
            "Data was successfully saved.",
            status_code
            )
