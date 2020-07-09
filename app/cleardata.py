#!/usr/bin/python3
# -*- coding: Utf-8 -*

from app.requestapi import ResquestApi


class ClearData(ResquestApi):
    """This class converts the retrieved data"""

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
