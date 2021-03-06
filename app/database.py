#!/usr/bin/python3
# -*- coding: Utf-8 -*

from config import config
import mysql.connector


class Database:
    """This class allows to communicate with the mysql database.
    This class is used to communicate with the mysql database.
    It allows to retrieve information and update the database.

    """

    def __init__(self):
        self.host = config.SERVER_ADRESS
        self.user = config.SERVER_USER_NAME
        self.password = config.SERVER_PASSWORD
        self.database = config.SERVER_DATABASE

    def create_database(self, sql_script):
        """Method to create the database tables"""
        self.start_connection()
        with open(sql_script, "r") as sql_script:
            read_file = sql_script.read()
            sql_commands = read_file.split(';')
            for command in sql_commands:
                try:
                    if command.strip() != '':
                        self.cursor.execute(command)
                except IOError as exception:
                    print("Command skipped: ", exception)
        self.mysql_connection.commit()
        self.close_connection()

    def start_connection(self):
        """Method to start connection with MySQL"""
        self.mysql_connection = mysql.connector.connect(host=self.host,
                                                        user=self.user,
                                                        password=self.password,
                                                        database=self.database)
        self.cursor = self.mysql_connection.cursor()

    def close_connection(self):
        """Method to close connection with MySQL"""
        self.cursor.close()
        self.mysql_connection.close()
