import csv
import os
import zipfile

from backend import app
from backend.models import db, Demographic, Location, LocationLookup
from backend.tools.dao.entity_dao import DemographicDAO, LocationLookupDAO, LocationDAO, DAO
from backend.tools.validator.bootstrap_validator import DemographicValidator, LocationValidator, LocationLookupValidator


class BootstrapManager():
    BOOTSTRAP_FILES_NAMES = ["demographics.csv", "location.csv", "location-lookup.csv"]

    @staticmethod
    def check_valid_files(zip_file):
        boostrap_zip_file = zipfile.ZipFile(zip_file)
        files_inside_zip = []
        for file in boostrap_zip_file.namelist():
            files_inside_zip.append(boostrap_zip_file.getinfo(file).filename)
        boostrap_zip_file.close()
        if set(files_inside_zip) == set(BootstrapManager.BOOTSTRAP_FILES_NAMES):
            return True
        else:
            return False

    @staticmethod
    def unzip_files(zip_file):
        path_to_extract_file = os.path.join(app.config['EXTRACT_FOLDER'])
        with zipfile.ZipFile(zip_file, 'r') as zipObj:
            # Extract all the contents of zip file in different directory
            zipObj.extractall(path_to_extract_file)

    @staticmethod
    def clean_up_db():
        try:
            db.session.query(Demographic).delete()
            db.session.query(Location).delete()
            db.session.query(LocationLookup).delete()
            db.session.commit()
        except:
            db.session.rollback()

    @staticmethod
    def import_files(file_name):
        dao = None
        validator = None
        all_error_msgs = {}
        records_to_import = {file_name: []}

        if file_name == DemographicDAO.FILE_NAME:
            dao = DemographicDAO()
            validator = DemographicValidator()
        elif file_name == LocationDAO.FILE_NAME:
            dao = LocationDAO()
            validator = LocationValidator()
            LocationLookupDAO.retrieve_valid_location_ids()
        else:
            dao = LocationLookupDAO()
            validator = LocationLookupValidator()
        with open(os.path.join(app.config['EXTRACT_FOLDER'], file_name)) as csv_file:
            row_number = 1
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_line = True
            for row in csv_reader:
                row_map = {}
                if first_line:
                    first_line = False
                    continue
                for index, attribute in enumerate(dao.CSV_COL_ORDER):
                    row_map[attribute] = row[index]
                error_msg = validator.is_valid(row_map)
                if len(error_msg) > 0:
                    all_error_msgs[row_number] = error_msg
                else:
                    records_to_import[file_name].append(row_map)
                row_number += 1
        # print(records_to_import)
        DAO.bulk_import_data(records_to_import)
