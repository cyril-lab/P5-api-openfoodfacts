#!/usr/bin/python3
# -*- coding: Utf-8 -*

from app.database import Database
import mysql.connector


class Substitution(Database):
    """This class allows to communicate with the substitution table"""

    def save_product_substitute(self, id_product, id_product_substitution):
        """Method to save the substitute products in the database"""
        try:
            self.start_connection()
            self.cursor.execute(f"""
            INSERT INTO substitution (Product_id, Product_sub)
                VALUES("{id_product}", "{id_product_substitution}");
            """)
            self.mysql_connection.commit()
            self.close_connection()
        except mysql.connector.IntegrityError as err:
            print("Une erreur est survenue. Error: {}".format(err))

    def get_substitution(self):
        """Method to retrieve substitute products from the database"""
        self.start_connection()
        self.cursor.execute(f"""SELECT * FROM substitution""")
        substitution = self.cursor.fetchall()
        self.close_connection()
        return substitution
