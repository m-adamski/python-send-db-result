import os
import sys
import argparse
import smtplib
import config.config as config_module


def main():
    # Define Argument Parser
    parser = argparse.ArgumentParser(description="Generate an Excel file containing the result of the SQL query")
    parser.add_argument("query", type=str, help="Path to the file containing the query to be executed")
    parser.add_argument("--config", type=str, help="Path to the configuration file")

    # Add database arguments
    database_group = parser.add_argument_group("database arguments")
    database_group.add_argument("--db-host", type=str, help="The host name or IP address of the MySQL server")
    database_group.add_argument("--db-port", type=int, help="The TCP/IP port of the MySQL server. Must be an integer")
    database_group.add_argument("--db-user", type=str, help="The user name used to authenticate with the MySQL server")
    database_group.add_argument("--db-password", type=str, help="The password to authenticate the user with the MySQL server")
    database_group.add_argument("--db-database", type=str, help="The database name to use when connecting with the MySQL server")
    database_group.add_argument("--db-charset", type=str, help="Which MySQL character set to use")
    database_group.add_argument("--db-collation", type=str, help="Which MySQL collation to use")

    # Add SMTP arguments
    smtp_group = parser.add_argument_group("smtp arguments")
    smtp_group.add_argument("--smtp-server", type=str, help="The host name of the SMTP server")
    smtp_group.add_argument("--smtp-port", type=int, help="The TCP/IP port of the SMTP server. Must be an integer")
    smtp_group.add_argument("--smtp-user", type=str, help="The user name used to authenticate with the SMTP server")
    smtp_group.add_argument("--smtp-password", type=str, help="The password to authenticate the user with the SMTP server")

    # Parse provided arguments
    try:
        arguments = parser.parse_args()

        # Make sure that SQL query file exists
        if os.path.isfile(arguments.query):
            config = config_module.Config(arguments)

        else:
            print("The file containing the query was not found in provided path")
            sys.exit(1)
    except argparse.ArgumentError:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
