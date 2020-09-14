# Send the SQL query result via SMTP

The script was created to automate the process of generating reports directly from the database and sending the result via e-mail.

## Installation

The module uses additional packages that must be installed with the package installer for Python. To do this, run the command:

```commandline
pip install -r requirements.txt
```

or by using the make utility:

```commandline
make install
```

## Virtual environment

The venv module provides support for creating "virtual environments" with your own independent set of Python packages. In order to prepare a virtual environment, we must first create it and then connect to it:

```commandline
python -m venv ./venv && source ./venv/Scripts/activate
```

or by using the make utility:

```commandline
make venv
```

**Instead of installing packages globally, we can only install them in a created virtual environment.**

In order to run the module with automatic connection to the virtual environment, the ``bin/run-venv.sh`` file has been prepared. Just run the command in the console:

```commandline
bin/run-venv.sh "SELECT * FROM table" --config-file=config/config.json
```

```commandline
bin/run-venv.sh query/sample-query.sql --config-file=config/config.json
```

## Configuration

The easiest way to configure the module is to create a JSON configuration file, similar to the sample file in the ``config`` folder. All configuration parameters can be overridden with arguments when starting the module.

## Running the module

```commandline
python main "SELECT * FROM table" --config-file=config/config.json
```

```commandline
python main query/sample-query.sql --config-file=config/config.json
```

## Arguments

Arguments given in the console override the values given in the configuration file.

``` commandline
usage: main [-h] [--config-file CONFIG_FILE] [--db-host DB_HOST] [--db-port DB_PORT] [--db-user DB_USER] [--db-password DB_PASSWORD] [--db-database DB_DATABASE] [--db-charset DB_CHARSET] [--db-collation DB_COLLATION] [--smtp-server SMTP_SERVER]
            [--smtp-port SMTP_PORT] [--smtp-protocol SMTP_PROTOCOL] [--smtp-timeout SMTP_TIMEOUT] [--smtp-user SMTP_USER] [--smtp-password SMTP_PASSWORD] [--smtp-sender SMTP_SENDER] [--smtp-receiver SMTP_RECEIVER] [--smtp-subject SMTP_SUBJECT]
            [--smtp-message SMTP_MESSAGE] [--smtp-attachment SMTP_ATTACHMENT]
            query

positional arguments:
  query                 SQL query or path to the file containing the SQL query

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        Path to the configuration file

database arguments:
  --db-host DB_HOST     The host name or IP address of the MySQL server
  --db-port DB_PORT     The TCP/IP port of the MySQL server. Must be an integer
  --db-user DB_USER     The user name used to authenticate with the MySQL server
  --db-password DB_PASSWORD
                        The password to authenticate the user with the MySQL server
  --db-database DB_DATABASE
                        The database name to use when connecting with the MySQL server
  --db-charset DB_CHARSET
                        Which MySQL character set to use
  --db-collation DB_COLLATION
                        Which MySQL collation to use

smtp arguments:
  --smtp-server SMTP_SERVER
                        The host name or IP address of the SMTP server
  --smtp-port SMTP_PORT
                        The TCP/IP port of the SMTP server. Must be an integer
  --smtp-protocol SMTP_PROTOCOL
                        Encryption protocol (only STARTTLS supported)
  --smtp-timeout SMTP_TIMEOUT
                        Timeout in seconds for blocking operations like the connection attempt
  --smtp-user SMTP_USER
                        The user name used to authenticate with the SMTP server
  --smtp-password SMTP_PASSWORD
                        The password to authenticate the user with the SMTP server
  --smtp-sender SMTP_SENDER
                        The email address of the sender
  --smtp-receiver SMTP_RECEIVER
                        Email addresses of the message recipients (separated by a comma)
  --smtp-subject SMTP_SUBJECT
                        Message subject
  --smtp-message SMTP_MESSAGE
                        Body of the message sent as plain text
  --smtp-attachment SMTP_ATTACHMENT
                        Name of the file that will be attached (add the extension .xlsx)
```

## Requirements

* python > 3.8
* mysql-connector-python > 8.0
* openpyxl > 3.0

## License

MIT
