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

        #executeScriptsFromFile(sql_script)
        self.mysql_connection.commit()


    def saved_category(self):
        
        cursor = self.mysql_connection.cursor()
        for element in config.CATEGORIES:
            cursor.execute(f"""INSERT INTO category (name) VALUES ("{element}")""")
        self.mysql_connection.commit()
        


    def saved_product(self, liste_product, number_catgory):
        product_list = sorted(liste_product, key=lambda colonnes: colonnes[3])
        cursor = self.mysql_connection.cursor()
        for element in product_list:
            cursor.execute(f"""
            INSERT INTO product (name, store, url, nutriscore_grade, Category_id)
                VALUES("{element[0]}", "{element[1]}", "{element[2]}", "{element[3]}", "{number_catgory}"
            );
            """)
        self.mysql_connection.commit()
        #self.mysql_connection.close()



category_pizzas = ClearData("fromages")
category_pizzas.get_number_products()
category_pizzas.calculate_number_page()
category_pizzas.get_data_api()
category_pizzas.generate_products_list()


mysql = Database("localhost", "cyril", "qsdf678/", "p5" )
mysql.create_database("p5.sql")
mysql.saved_category()

mysql.saved_product(category_pizzas.products, 1)


#print(category_pizzas.products)

