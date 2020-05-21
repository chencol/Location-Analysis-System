from datetime import datetime

from backend.models import Demographic, LocationLookup, Location, db


class DAO():
    @staticmethod
    def bulk_import_data(records_to_import):
        for file_name in records_to_import:
            if file_name == DemographicDAO.FILE_NAME:
                entity = Demographic()
            elif file_name == LocationLookupDAO.FILE_NAME:
                entity = LocationLookup()
            else:
                entity = Location()
            fourth_time = datetime.utcnow()
            db.session.execute(
                entity.__table__.insert(),
                records_to_import[file_name]
            )
            db.session.commit()
            five_time = datetime.utcnow()
            print((five_time - fourth_time).total_seconds())


class DemographicDAO(DAO):
    FILE_NAME = "demographics.csv"
    TABLE_NAME = "demographic"
    MAC_ADDRESS_COL_NAME = "mac_address"
    NAME_COL_NAME = "name"
    PASSWORD_COL_NAME = "password"
    EMAIL_COL_NAME = "email"
    GENDER_COL_NAME = "gender"
    CSV_COL_ORDER = [MAC_ADDRESS_COL_NAME, NAME_COL_NAME, PASSWORD_COL_NAME, EMAIL_COL_NAME, GENDER_COL_NAME]


class LocationDAO(DAO):
    FILE_NAME = "location.csv"
    TABLE_NAME = "location"
    TIMESTAMP_COL_NAME = "timestamp"
    MACADDRESS_COL_NAME = "mac_address"
    LOCATION_ID_COL_NAME = "location_id"
    CSV_COL_ORDER = [TIMESTAMP_COL_NAME, MACADDRESS_COL_NAME, LOCATION_ID_COL_NAME]


class LocationLookupDAO(DAO):
    FILE_NAME = "location-lookup.csv"
    TABLE_NAME = "location_lookup"
    LOCATION_ID_COL_NAME = "location_id"
    SEMANTIC_PLACE_COL_NAME = "semantic_place"
    CSV_COL_ORDER = [LOCATION_ID_COL_NAME, SEMANTIC_PLACE_COL_NAME]
    valid_location_ids = None

    @staticmethod
    def retrieve_valid_location_ids():
        sql = 'select location_id from location_lookup;'
        location_lookups = db.session.execute(sql).fetchall()
        result = [location_lookup[0] for location_lookup in location_lookups]
        LocationLookupDAO.valid_location_ids = result
