#!/usr/bin/python3
# -*- coding: Utf-8 -*

from app.database import Database


class Product(Database):
    """This class allows to communicate with the product table"""

    def save_product(self, list_product, number_category):
        """Method to save the products in the database"""
        self.get_connection()
        self.create_cursor()
        product_list = sorted(list_product, key=lambda colonnes: colonnes[3])
        for element in product_list:
            self.cursor.execute(f"""
            INSERT INTO product (name, store, url, nutriscore_grade,
                                 Category_id)
                VALUES("{element[0]}", "{element[1]}", "{element[2]}",
                       "{element[3]}", "{number_category}");
            """)
        self.mysql_connection.commit()
        self.close_cursor()
        self.close_connection()

    def get_list_product(self, category_number):
        """Method to retrieve the list of products from the database"""
        self.get_connection()
        self.create_cursor()
        self.cursor.execute(f"""
            SELECT * FROM product
            WHERE Category_id = {category_number} ORDER BY id""")
        list_product = self.cursor.fetchall()
        self.close_cursor()
        self.close_connection()
        return list_product

    def get_product(self, id_product):
        """Method to retrieve one product from the database"""
        self.get_connection()
        self.create_cursor()
        self.cursor.execute(f"""
            SELECT *  FROM product WHERE id = {id_product}""")
        product = self.cursor.fetchall()
        self.close_cursor()
        self.close_connection()
        return product
