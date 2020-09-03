import mysql.connector
from mysql.connector import errorcode


def execute(config, query):
    try:

        # Create connection
        connection = mysql.connector.connect(
            host=config.db_host,
            port=config.db_port,
            user=config.db_user,
            password=config.db_password,
            database=config.db_database,
            charset=config.db_charset,
            collation=config.db_collation
        )

        # Create cursor and execute provided query
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch result
        result = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        connection.close()

        return result

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
