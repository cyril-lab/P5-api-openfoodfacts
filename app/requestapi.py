#!/usr/bin/python3
# -*- coding: Utf-8 -*

import lang.fr as fr
from config import config
import math
import requests


class ResquestApi:
    """This class is used to download data from open food facts.
    This class downloads data from the website open food facts using the API.
    Multiple requests are sent until the maximum number entered
    or the number of products is expected.

    """

    def __init__(self, category):
        self.number_products_max = config.NUMBER_PRODUCT_MAX
        self.category = category
        self.number_products = self._get_number_products()
        self.number_page = 1
        self.results_page = config.PRODUCT_PAGE
        self.data_category_json = []

    def _get_number_products(self):
        """method to get the number of products in the category"""
        number_product_category = requests.get(
            f"https://fr.openfoodfacts.org/categorie/{self.category}.json")
        number_product_category_json = number_product_category.json()
        return int(number_product_category_json["count"])

    def _calculate_number_page(self):
        """method to calculate the number of pages required for the request"""
        if self.number_products > self.results_page:
            self.number_page = (math.ceil(min(
                self.number_products,
                self.number_products_max) / self.results_page))
            return self.number_page

    def get_data_api(self):
        """method to get data produts"""
        number_page = self._calculate_number_page()
        while number_page:
            print(f"Téléchargement de {self.results_page} "
                  f"produits {self.category} "
                  f"(requête {(self.number_page-number_page+1)}"
                  f"/{self.number_page}) ...")
            data_category = requests.get(
                f"https://fr.openfoodfacts.org/cgi/search.pl?action=process"
                f"&tagtype_0=categories&tag_contains_0=contains&"
                f"tag_0={self.category}&page_size={self.results_page}"
                f"&page={number_page}&json=1")

            if data_category.status_code == 200:
                print(fr.FR[16])
            elif data_category.status_code == 400 or \
                    data_category.status_code == 500:
                print(fr.FR[17])
            else:
                print(fr.FR[18], data_category.status_code)
            self.data_category_json.append(data_category.json())
            number_page -= 1
