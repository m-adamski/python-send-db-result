import os
import json


def load_config_file(config_path):
    if config_path is not None and os.path.isfile(config_path):
        with open(config_path, "r") as config_file:
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
    db_charset = "utf8mb4"
    db_collation = "utf8mb4_unicode_ci"

    # SMTP configuration
    smtp_server = ""
    smtp_port = 587
    smtp_protocol = "STARTTLS"
    smtp_timeout = 10
    smtp_user = ""
    smtp_password = ""
    smtp_sender = ""
    smtp_receiver = ""
    smtp_subject = ""
    smtp_message = ""
    smtp_attachment = "report.xlsx"

    def __init__(self, arguments):
        # Read config file
        config_data = load_config_file(arguments.config_file)

        # Overwrite configuration
        # Arguments provided in console overwrite this provided in config file
        # Need to use vars() function because arguments object is type 'Namespace' which is not iterable
        self.overwrite(config_data)
        self.overwrite(vars(arguments))

    def overwrite(self, data):
        for category in data:

            # When provided config file data
            if type(data[category]) is dict:
                for item in data[category]:
                    param = category + "_" + item
                    value = data[category][item]

                    if hasattr(self, param) and value is not None:
                        setattr(self, param, value)

            # When provided arguments from console
            elif type(data[category]) is str:
                param = category
                value = data[category]

                if hasattr(self, param) and value is not None:
                    setattr(self, param, value)

    def dump(self):
        return {
            "db-host": self.db_host,
            "db-port": self.db_port,
            "db-user": self.db_user,
            "db-password": self.db_password,
            "db-database": self.db_database,
            "db-charset": self.db_charset,
            "db-collation": self.db_collation,
            "smtp-server": self.smtp_server,
            "smtp-port": self.smtp_port,
            "smtp-protocol": self.smtp_protocol,
            "smtp-timeout": self.smtp_timeout,
            "smtp-user": self.smtp_user,
            "smtp-password": self.smtp_password,
            "smtp-sender": self.smtp_sender,
            "smtp-receiver": self.smtp_receiver,
            "smtp-subject": self.smtp_subject,
            "smtp-message": self.smtp_message,
            "smtp-attachment": self.smtp_attachment
        }
