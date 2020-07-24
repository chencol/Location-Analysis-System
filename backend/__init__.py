import os
import platform
from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
SESSION_TYPE = "redis"
app.debug = True
app.config.from_object(__name__)
# app.config["SECRET_KEY"] = os.urandom(24)
# app.config["SECRET_KEY"] = "testingsession"
# app.secret_key = "DragonFire"
os_sys = platform.system()
db_name = "flask1"
UPLOAD_FOLDER = "/usr/local/file_storage/temp"
EXTRACT_FOLDER = "/usr/local/file_storage/temp/bootstrap_files"
if os_sys == "Windows":
    db_name = "flask2"
    UPLOAD_FOLDER = "file_storage\\temp"
    EXTRACT_FOLDER = "file_storage\\temp\\bootstrap_files"
app.secret_key = "why would I tell you my secret key?"
ALLOWED_EXTENSIONS = {"zip"}
CORS(app, supports_credentials=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["EXTRACT_FOLDER"] = EXTRACT_FOLDER
app.config["JSON_SORT_KEYS"] = False

from backend import views
from backend.controller import user_handler
from backend.tools.bootstrap import bootstrap_endpoint
from backend.tools.api import product_endpoint
from backend.tools.api import purchase_record_endpoint
from backend.tools.api import favor_endpoint
from backend.tools.entity.demographic_endpoint import demographic
