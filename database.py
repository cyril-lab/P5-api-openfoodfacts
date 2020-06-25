#!/usr/bin/python3
# -*- coding: Utf-8 -*

import mysql.connector 

from cleardata import ClearData
import config

class Database:

    def __init__(self, host, user, password, database):
        self.mysql_connection = mysql.connector.connect(host=host,
                                                user=user,
                                                password=password,
                                                database=database)

    def create_database(self, sql_script):
        cursor = self.mysql_connection.cursor()
        with open(sql_script, "r") as sql_script:
            read_file = sql_script.read()
            sql_commands = read_file.split(';')
            for command in sql_commands:
                try:
                    if command.strip() != '':
                        cursor.execute(command)
                except IOError as exception:
                    print("Command skipped: ", exception)
        self.mysql_connection.commit()


    def saved_category(self):
        cursor = self.mysql_connection.cursor()
        for element in config.CATEGORIES:
            cursor.execute(f"""INSERT INTO category (name) VALUES ("{element}")""")
        self.mysql_connection.commit()
        
    def saved_product(self, liste_product, number_category):
        product_list = sorted(liste_product, key=lambda colonnes: colonnes[3])
        cursor = self.mysql_connection.cursor()
        for element in product_list:
            cursor.execute(f"""
            INSERT INTO product (name, store, url, nutriscore_grade, Category_id)
                VALUES("{element[0]}", "{element[1]}", "{element[2]}", "{element[3]}", "{number_category}"
            );
            """)
        self.mysql_connection.commit()
        #self.mysql_connection.close()

    def saved_product_substitution(self, id_product, id_product_substitution):
        cursor = self.mysql_connection.cursor()
        cursor.execute(f"""
        INSERT INTO substitution (Product_id, Product_sub)
            VALUES("{id_product}", "{id_product_substitution}"
        );
        """)
        self.mysql_connection.commit()    

    def get_list_product(self, category_number):
        cursor = self.mysql_connection.cursor()
        cursor.execute(f"""SELECT * FROM product WHERE Category_id = {category_number} ORDER BY id""")
        tup = cursor.fetchall()
        return tup

    def get_substitution(self):
        cursor = self.mysql_connection.cursor()
        cursor.execute(f"""SELECT * FROM substitution""")
        tup = cursor.fetchall()
        return tup

    def get_product(self, id_product):
        cursor = self.mysql_connection.cursor()
        cursor.execute(f"""SELECT *  FROM product WHERE id = {id_product}""")
        tup = cursor.fetchall()
        return tup

