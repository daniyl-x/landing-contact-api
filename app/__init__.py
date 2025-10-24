import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from app.routes.api import api
from app.routes.browser import browser


app = Flask(__name__, instance_relative_config=True)
os.makedirs(app.instance_path, exist_ok=True)

app.config.from_object("app.default_config")
app.config.from_pyfile("config.py", silent=True)

app.config["OUTPUT_PATH"] = os.path.join(
        app.instance_path,
        app.config["OUTPUT_FILENAME"]
        )


PROXY_COUNT = app.config["PROXY_COUNT"]
app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=PROXY_COUNT,
        x_proto=PROXY_COUNT,
        x_host=PROXY_COUNT,
        x_prefix=PROXY_COUNT,
        )


app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(browser, url_prefix="/")
