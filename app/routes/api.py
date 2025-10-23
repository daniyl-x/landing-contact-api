import os
import csv
from flask import Blueprint, request, current_app


api = Blueprint("browser", __name__)


@api.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@api.post("/post")
def post():
    CSV_FIELDS = current_app.config["CSV_FIELDS"]
    data_error_msg = (
            "Please send data containing values in the next fields: "
            f"{CSV_FIELDS}."
            )

    data = request.get_json()
    if not data:
        reponse = {
                "status": "error",
                "message": f"No data was provided. {data_error_msg}"
                }
        return reponse, 400

    csv_data = {key: data.get(key) for key in CSV_FIELDS}
    if not any(csv_data.values()):
        reponse = {
                "status": "error",
                "message": f"All expected fields are empty. {data_error_msg}"
                }
        return reponse, 422

    OUTPUT_PATH = current_app.config["OUTPUT_PATH"]
    status_code = 200
    response = {"status": "success", "message": "Data was successfully saved."}

    if not os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH, "w", newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=CSV_FIELDS)
            writer.writeheader()
        status_code = 201

    with open(OUTPUT_PATH, "a", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=CSV_FIELDS)
        writer.writerow(csv_data)

    return response, status_code
