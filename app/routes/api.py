import os
import csv
from flask import Blueprint, request, current_app


api = Blueprint("browser", __name__)


@api.get("/healthcheck")
def healthcheck():
    return {"is_alive": True}


@api.post("/post")
def post():
    data = request.get_json()
    if not data:
        return "No data provided.", 400

    OUTPUT_PATH = current_app.config["OUTPUT_PATH"]
    CSV_FIELDS = current_app.config["CSV_FIELDS"]
    if not os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH, "w", newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=CSV_FIELDS)
            writer.writeheader()

    with open(OUTPUT_PATH, "a", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=CSV_FIELDS)
        writer.writerow({key: data.get(key) for key in CSV_FIELDS})

    return "Data appended successfully."
