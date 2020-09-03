import os
import json


def load_config_file(config_path):
    if config_path is not None and os.path.isfile(config_path):
        with open(config_path) as config_file:
            return json.load(config_file)
    else:
        return {}


class Config:
    # Database configuration
    db_host = "127.0.0.1"
    db_port = 3306
    db_user = ""
    db_password = ""
    db_database = ""
    db_charset = "utf-8"
    db_collation = "utf8mb4_unicode_ci"

    # SMTP configuration
    smtp_server = ""
    smtp_port = 587
    smtp_user = ""
    smtp_password = ""

    # Configuration parameters mapping
    mapping = {
        "db-host": "db_host",
        "db-port": "db_port",
        "db-user": "db_user",
        "db-password": "db_password",
        "db-database": "db_database",
        "db-charset": "db_charset",
        "db-collation": "db_collation",
        "smtp-server": "smtp_server",
        "smtp-port": "smtp_port",
        "smtp-user": "smtp_user",
        "smtp-password": "smtp_password"
    }

    def __init__(self, arguments):
        # Read config file
        config_data = load_config_file(arguments.config)

        # Overwrite configuration
        # Arguments provided in console overwrite this provided in config file
        # Need to use vars() function because arguments object is type 'Namespace' which is not iterable
        self.overwrite(config_data, self.mapping)
        self.overwrite(vars(arguments), self.mapping)

    def overwrite(self, data, mapping):
        for category in data:

            # When provided config file data
            if type(data[category]) is dict:
                for item in data[category]:
                    param = category + "-" + item
                    value = data[category][item]

                    # Change value of Config parameter
                    if param in mapping and value is not None:
                        setattr(self, mapping[param], value)

            # When provided arguments from console
            elif type(data[category]) is str:
                param = category
                value = data[category]

                # Change value of Config parameter
                if param in mapping and value is not None:
                    setattr(self, mapping[param], value)
