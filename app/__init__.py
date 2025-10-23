import os
from flask import Flask

from app.routes.api import api


app = Flask(__name__)

# TODO: add instance settings
app.config.from_object("app.default_settings")
app.config["OUTPUT_PATH"] = os.path.join(
        app.instance_path,
        app.config["OUTPUT_FILENAME"]
        )

os.makedirs(app.instance_path, exist_ok=True)

app.register_blueprint(api, url_prefix="/api")
