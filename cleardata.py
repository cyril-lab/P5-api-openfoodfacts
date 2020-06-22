#!/usr/bin/python3
# -*- coding: Utf-8 -*

import config
from requestapi import ResquestApi


class ClearData(ResquestApi):
    """This class converts the retrieved data."""

    def __init__(self, category):
        ResquestApi.__init__(self, category)
        self.products = []

    def generate_products_list(self):
        """method to generate a list with products"""
        for request in self.data_category_json:
            for product in request["products"]:
                if product.get("product_name_fr") \
                        and product.get("stores") \
                        and product.get("url") \
                        and product.get("nutriscore_grade") is not None \
                        and len(self.products) < self.number_products_max:

                    self.products.extend([[product.get("product_name_fr"),
                                           product.get("stores"),
                                           product.get("url"),
                                           product.get("nutriscore_grade")]])
"""

category_pizzas = ClearData("fromages")
category_pizzas.get_number_products()
category_pizzas.calculate_number_page()
category_pizzas.get_data_api()
category_pizzas.generate_products_list()

print(category_pizzas.products)
print(len(category_pizzas.products))
print(len(category_pizzas.data_category_json))
"""