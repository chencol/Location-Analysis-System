import os
from pathlib import Path

from flask import flash, request, jsonify
from werkzeug.utils import secure_filename

from backend import app, ALLOWED_EXTENSIONS
from backend.controller.user_handler import is_user_authenticated
from backend.tools.bootstrap.bootstrap import BootstrapManager
from backend.tools.dao.entity_dao import DemographicDAO, LocationLookupDAO, LocationDAO


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_files', methods=['POST'])
def upload_file():
    if is_user_authenticated():
        if 'file' not in request.files:
            flash('No file part')
            return jsonify(status="Failed", error_msg="No file part has been upload!")
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify(status="Failed", error_msg="No file has been upload!")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # currentDirectory = os.getcwd()
            # path_to_save_file = os.path.join(currentDirectory + app.config['UPLOAD_FOLDER'] + filename)
            # file.save(path_to_save_file)
            # U can't add slash in front of it.
            if BootstrapManager.check_valid_files(file):
                path_to_save_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path_to_save_file)
                try:
                    BootstrapManager.unzip_files(file)
                    try:
                        BootstrapManager.clean_up_db()
                        BootstrapManager.import_files(DemographicDAO.FILE_NAME)
                        BootstrapManager.import_files(LocationLookupDAO.FILE_NAME)
                        BootstrapManager.import_files(LocationDAO.FILE_NAME)
                        return jsonify(status="Successful")
                    except:
                        return jsonify(status="Failed", error_msg="Exception occur when inserting data into database!")
                except:
                    return jsonify(status="Failed",
                                   error_msg="File cannot be unzip properly! Make sure your zip file is not corrupted!")
                # BootstrapManager.import_files(DemographicDAO.FILE_NAME)
                # BootstrapManager.import_files(LocationLookupDAO.FILE_NAME)
                # BootstrapManager.import_files(LocationDAO.FILE_NAME)
                return jsonify(status="Successful")
            else:
                return jsonify(status="Failed", error_msg="Contain invalid files!")
        else:
            return jsonify(status="Failed", error_msg="Only zip file is allowed to upload!")
    else:
        return jsonify(status="Failed", error_msg="Unauthorized action")
