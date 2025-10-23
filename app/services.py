import csv


class ValidationError(Exception):
    def __init__(self, message, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


def make_response(
        status: str,
        message: str,
        status_code: int
        ) -> tuple[dict, int]:
    return {"status": status, "message": message}, status_code


def validate_data(data: dict, csv_fields: list) -> dict:
    data_error_msg = (
            "Please provide data containing values in the next fields: "
            f"{csv_fields}."
            )

    if not data:
        raise ValidationError(f"No data was provided. {data_error_msg}")

    csv_data = {key: data.get(key) for key in csv_fields}
    if not any(csv_data.values()):
        raise ValidationError(
                f"All expected fields are empty. {data_error_msg}"
                )

    return csv_data


def write_csv_header(csv_path: str, fieldnames: list) -> None:
    with open(csv_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def write_csv_row(csv_path: str, csv_data: dict, fieldnames: list) -> None:
    with open(csv_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(csv_data)
