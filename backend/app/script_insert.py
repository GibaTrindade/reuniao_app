import mysql.connector
from .config import settings

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(name, image, description):
    print("Inserting BLOB into aircraft table")
    try:
        connection = mysql.connector.connect(host=settings.BD_HOST, database=settings.BD_DATABASE,
                                             user=settings.BD_USER, password=settings.BD_PASSWORD)

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO aircraft
                          (name, image, description) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(image)

        # Convert data into tuple format
        insert_blob_tuple = (name, empPicture, description)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into aircraft table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB("AircraftTest", "./static/images/challenger_350_datauri",
           "Testing insert blob")