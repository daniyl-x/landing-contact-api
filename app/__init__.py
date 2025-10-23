import os
from flask import Flask

from app.routes.api import api


app = Flask(__name__, instance_relative_config=True)
os.makedirs(app.instance_path, exist_ok=True)

app.config.from_object("app.default_config")
app.config.from_pyfile("config.py", silent=True)

app.config["OUTPUT_PATH"] = os.path.join(
        app.instance_path,
        app.config["OUTPUT_FILENAME"]
        )


app.register_blueprint(api, url_prefix="/api")
