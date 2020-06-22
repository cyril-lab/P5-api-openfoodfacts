#!/usr/bin/python3
# -*- coding: Utf-8 -*


import config
import requests
import math


class ResquestApi:
    """Download data from open food facts.
    This class downloads data from the website open food facts using the API.
    Multiple requests are sent until the maximum number entered
    or the number of products is expected.

    """

    def __init__(self, category):
        self.number_products_max = config.NUMBER_PRODUCT_MAX
        self.category = category
        self.number_products = 0
        self.number_page = 1
        self.results_page = config.NUMBER_PRODUCT
        self.data_category_json = []

    def calculate_number_page(self):
        """method to calculate the number of pages required for the request"""
        if self.number_products > self.results_page:
            self.number_page = (math.ceil(min(
                
                self.number_products,
                self.number_products_max) / self.results_page))

    def get_number_products(self):
        """method to get the number of products in the category"""
        number_product_category = requests.get(
            f"https://fr.openfoodfacts.org/categorie/{self.category}.json")
        number_product_category_json = number_product_category.json()
        self.number_products = int(number_product_category_json["count"])

    def get_data_api(self):
        """method to get data produts"""
        number_page = self.number_page

        while number_page:
            data_category = requests.get(
                f"https://fr.openfoodfacts.org/cgi/search.pl?action=process"
                f"&tagtype_0=categories&tag_contains_0=contains&"
                f"tag_0={self.category}&page_size={self.results_page}"
                f"&page={number_page}&json=1")

            self.data_category_json.append(data_category.json())
            number_page -= 1
