from abc import ABC, abstractmethod
import re

from backend.tools.dao.entity_dao import DemographicDAO, LocationLookupDAO


class Validator:
    def is_valid(self, row_map):
        error_msg = []
        for attribute in row_map:
            if not self.check_blank(row_map[attribute]):
                error_msg.append(attribute + " is blank")
        if len(error_msg) != 0:
            return error_msg
        else:
            for attribute in row_map:
                if attribute != "name":
                    if not getattr(self, "check_" + attribute)(row_map[attribute]):
                        error_msg.append("Invalid " + attribute)
            # if len(error_msg) != 0:
            #     print(row_map)
            #     print(error_msg)
            return error_msg

    def check_mac_address(self, mac_address):
        pattern = "[a-fA-F0-9]{40}$"
        is_matched = re.match(pattern, mac_address)
        if is_matched:
            return True
        else:
            return False

    def check_blank(self, attribute):
        if attribute == "":
            return False
        else:
            return True


class DemographicValidator(Validator):
    def check_email(self, email_address):
        pattern = "([a-zA-Z0-9]+(\\.){1})+[0-9]{4}(@){1}(business|accountancy|sis|economics|law|socsc){1}(\\.smu\\.edu\\.sg){1}"
        is_matched = re.match(pattern, email_address)
        if is_matched:
            return True
        else:
            return False

    def check_gender(self, gender):
        potential_gender_value = ["F", "M", "f", "m"]
        if gender in potential_gender_value:
            return True
        else:
            return False

    def check_password(self, password):
        if " " not in password and len(password) >= 8:
            return True
        else:
            return False


class LocationLookupValidator(Validator):
    def check_location_id(self, location_id):
        try:
            int(location_id)
            return True
        except:
            return False

    def check_semantic_place(self, semantic_place):
        pattern = "(SMUSISL|SMUSISB)([1-5]{1})(.+)"
        is_matched = re.match(pattern, semantic_place)
        if is_matched:
            return True
        else:
            return False


class LocationValidator(Validator):
    def check_timestamp(self, timestamp):
        pattern = "(\\d){4}-(\\d){2}-(\\d){2} (\\d){2}:(\\d){2}:(\\d){2}"
        is_matched = re.match(pattern, timestamp)
        if is_matched:
            return True
        else:
            return False

    def check_location_id(self, location_id):
        if location_id in LocationLookupDAO.valid_location_ids:
            return True
        else:
            return False
