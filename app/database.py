#!/usr/bin/python3
# -*- coding: Utf-8 -*

from config import config
import mysql.connector


class Database:
    """This class allows to communicate with the mysql database.
    This class is used to communicate with the mysql database.
    It allows to retrieve information and update the database.

    """

    def __init__(self, host, user, password, database):
        self.mysql_connection = mysql.connector.connect(host=host,
                                                        user=user,
                                                        password=password,
                                                        database=database)
        self.cursor = self.mysql_connection.cursor()

    def create_database(self, sql_script):
        """Method to create the database tables"""
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

    def save_category(self):
        """Method to save the categories in the database"""
        for element in config.CATEGORIES:
            self.cursor.execute(f"""
                INSERT INTO category (name) VALUES ("{element}")""")
        self.mysql_connection.commit()

    def save_product(self, list_product, number_category):
        """Method to save the products in the database"""
        product_list = sorted(list_product, key=lambda colonnes: colonnes[3])
        for element in product_list:
            self.cursor.execute(f"""
            INSERT INTO product (name, store, url, nutriscore_grade,
                                 Category_id)
                VALUES("{element[0]}", "{element[1]}", "{element[2]}",
                       "{element[3]}", "{number_category}");
            """)
        self.mysql_connection.commit()

    def save_product_substitute(self, id_product, id_product_substitution):
        """Method to save the substitute products in the database"""
        try:
            self.cursor.execute(f"""
            INSERT INTO substitution (Product_id, Product_sub)
                VALUES("{id_product}", "{id_product_substitution}");
            """)
            self.mysql_connection.commit()
        except mysql.connector.IntegrityError as err:
            print("Une erreur est survenue. Error: {}".format(err))

    def get_list_product(self, category_number):
        """Method to retrieve the list of products from the database"""
        self.cursor.execute(f"""
            SELECT * FROM product
            WHERE Category_id = {category_number} ORDER BY id""")
        list_product = self.cursor.fetchall()
        return list_product

    def get_substitution(self):
        """Method to retrieve substitute products from the database"""
        self.cursor.execute(f"""SELECT * FROM substitution""")
        substitution = self.cursor.fetchall()
        return substitution

    def get_product(self, id_product):
        """Method to retrieve one product from the database"""
        self.cursor.execute(f"""
            SELECT *  FROM product WHERE id = {id_product}""")
        product = self.cursor.fetchall()
        return product
