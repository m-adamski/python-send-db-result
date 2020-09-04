import os
import sys
import argparse
import datetime
import config.config as config_module
import database.mysql as mysql_module
import mailer.mailer as mailer_module
import workbook.workbook as workbook_module


def main():
    # Define Argument Parser
    parser = argparse.ArgumentParser(description="Generate an Excel file containing the result of the SQL query")
    parser.add_argument("query", type=str, help="SQL query or path to the file containing the SQL query")
    parser.add_argument("--config-file", type=str, help="Path to the configuration file")

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
    smtp_group.add_argument("--smtp-server", type=str, help="The host name or IP address of the SMTP server")
    smtp_group.add_argument("--smtp-port", type=int, help="The TCP/IP port of the SMTP server. Must be an integer")
    smtp_group.add_argument("--smtp-protocol", type=str, help="Encryption protocol (only STARTTLS supported)")
    smtp_group.add_argument("--smtp-timeout", type=int, help="Timeout in seconds for blocking operations like the connection attempt")
    smtp_group.add_argument("--smtp-user", type=str, help="The user name used to authenticate with the SMTP server")
    smtp_group.add_argument("--smtp-password", type=str, help="The password to authenticate the user with the SMTP server")
    smtp_group.add_argument("--smtp-sender", type=str, help="The email address of the sender")
    smtp_group.add_argument("--smtp-receiver", type=str, help="Email addresses of the message recipients (separated by a comma)")
    smtp_group.add_argument("--smtp-subject", type=str, help="Message subject")
    smtp_group.add_argument("--smtp-message", type=str, help="Body of the message sent as plain text")
    smtp_group.add_argument("--smtp-attachment", type=str, help="Name of the file that will be attached (add the extension .xlsx)")

    # Parse provided arguments
    try:
        print("Launch date: ", datetime.datetime.today())
        print("Reading the given arguments and generating the configuration")
        arguments = parser.parse_args()
        config = config_module.Config(arguments)
        query = arguments.query

        # Read provided file if query argument contains path to SQL file
        if os.path.isfile(arguments.query):
            print("Reading an SQL query file")
            query_handler = open(arguments.query, "r")
            query = query_handler.read()
            query_handler.close()

        # Execute query
        print("Running the SQL query")
        result = mysql_module.execute(config, query, True)

        # Receive stream from generated workbook
        if result is not None:
            print("Generating an Excel document")
            workbook_stream = workbook_module.write(result)

            # Generating message
            print("Sending a message")
            message = mailer_module.generate_message(config, workbook_stream)

            # Send message
            if message is not None:
                send_result = mailer_module.send(config, message)

                # Check sending status
                if send_result:
                    print("The message has been sent correctly")
                    exit(0)

    except argparse.ArgumentError:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
