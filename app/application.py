#!/usr/bin/python3
# -*- coding: Utf-8 -*

from app.cleardata import ClearData
from app.database import Database
from config import config
import lang.fr as fr


class Application:
    """This class manage the program display.
    This class manages the different menus of the program.

    """

    def __init__(self):
        self.mysql = Database(config.SERVER_ADRESS,
                              config.SERVER_USER_NAME,
                              config.SERVER_PASSWORD,
                              config.SERVER_DATABASE)
        self.category = ""
        self.products = []
        self.products_sub = []
        self.product_selected = []
        self.prod_sub = []
        self.leave_main_menu = 1
        self.leave_category_choice = 1
        self.leave_choice_product = 1
        self.leave_choice_sub = 1
        self.leave_saved_sub = 1
        self.first_number = 0
        self.choice_menu = ""
        self.input_product = ""
        self.product_sub = ""
        self.input_product_sub = ""

    def main(self):
        self.main_menu()

    def initialise_bdd(self):
        """Method to reset database and save categories"""
        print(fr.FR[1])
        self.mysql.create_database("sql/p5.sql")
        print(fr.FR[2])
        self.mysql.saved_category()
        print(fr.FR[3])

    def saved_product_bdd(self):
        """Method to retrieve the products and save them in the database"""
        for element in config.CATEGORIES:
            category = ClearData(element)
            category.get_data_api()
            category.generate_products_list()
            self.mysql.saved_product(category.products,
                                     config.CATEGORIES.index(element)+1)

    def main_menu(self):
        """Method to display the different choices of the main menu"""
        while self.leave_main_menu:
            print(fr.FR[4], fr.FR[5], fr.FR[6], fr.FR[7])
            self.choice_menu = input(fr.FR[8])
            self.main_menu_input()

    def main_menu_input(self):
        """Method to manage entries in the main menu"""
        if self.choice_menu == "1":
            self.category_choice()
        elif self.choice_menu == "2":
            print(fr.FR[9])
            for element in self.mysql.get_substitution():
                for substitution in element:
                    test = self.mysql.get_product(substitution)
                    print(test[0][1] + " - "
                          + test[0][2] + " - "
                          + test[0][3] + " - "
                          + test[0][4])
                print("\n")
        elif self.choice_menu == "3":
            self.initialise_bdd()
            self.saved_product_bdd()
        elif self.choice_menu == "4":
            self.leave_main_menu -= 1

    def category_choice(self):
        """Method to display the different choices in the categories menu"""
        self.leave_category_choice = 1
        while self.leave_category_choice:
            print(fr.FR[15])
            for element in config.CATEGORIES:
                print(str(config.CATEGORIES.index(element)+1)
                      + " : " + element)
            self.category_choice_input()

    def category_choice_input(self):
        """Method to manage entries in the categories menu"""
        self.category = input(fr.FR[8])
        if self.category == "q":
            self.leave_category_choice -= 1
        try:
            if 1 <= int(self.category) <= len(config.CATEGORIES):
                print(self.category)
                self.products = self.mysql.get_list_product(self.category)
                self.products_sub = self.mysql.get_list_product(self.category)
                self.choice_product()
                self.leave_category_choice -= 1
        except ValueError:
            pass

    def display_product(self, list_products):
        """Method to display the different choices in the products menu"""
        for element in list_products[self.first_number:self.first_number +
                                     config.NUMBER_PRODUCT_DISPLAY]:
            print(str(list_products.index(element) + 1)
                  + " - " + element[1] + " - " + element[4].upper()
                  + " - " + element[2] + " - " + element[3])

    def choice_product(self):
        self.first_number = 0
        self.leave_choice_product = 1
        while self.leave_choice_product:
            print(fr.FR[11])
            self.display_product(self.products)
            self.input_product = input(fr.FR[12])
            self.choice_product_input()

    def choice_product_input(self):
        """Method to manage entries in the products menu"""
        if self.input_product == "s" and (
                self.first_number + config.NUMBER_PRODUCT_DISPLAY)\
                < len(self.products):
            self.first_number += config.NUMBER_PRODUCT_DISPLAY
        elif self.input_product == "p" and self.first_number > 0:
            self.first_number -= config.NUMBER_PRODUCT_DISPLAY
        elif self.input_product == "q":
            self.leave_choice_product -= 1
        try:
            if 1 <= int(self.input_product) <= len(self.products):
                self.product_selected = self.products[int(self.input_product)
                                                      - 1][0]
                del self.products_sub[int(self.input_product)-1]
                self.choice_sub()
                self.leave_choice_product -= 1
        except ValueError:
            pass

    def choice_sub(self):
        """Method to display the different choices in the substitute menu"""
        self.first_number = 0
        self.leave_choice_sub = 1
        while self.leave_choice_sub:
            print(fr.FR[13])
            self.display_product(self.products_sub)
            self.input_product_sub = input(fr.FR[12])
            self.choice_sub_input()

    def choice_sub_input(self):
        """Method to manage entries in the substitute products menu"""
        if self.input_product_sub == "s" and (self.first_number +
                                              config.NUMBER_PRODUCT_DISPLAY) \
                < len(self.products_sub):
            self.first_number += 5
        elif self.input_product_sub == "p" and self.first_number > 0:
            self.first_number -= 5
        elif self.input_product_sub == "q":
            self.leave_choice_sub -= 1
        try:
            if 1 <= int(self.input_product_sub) <= len(self.products_sub):
                self.prod_sub = self.products_sub[int(self.input_product_sub)
                                                  - 1][0]
                self.saved_sub()
                self.leave_choice_sub -= 1
        except ValueError:
            pass

    def saved_sub(self):
        """Method to ask to the user if he wants to register the substitute"""
        self.leave_saved_sub = 1
        while self.leave_saved_sub:
            print(fr.FR[14])
            self.product_sub = input("y / n : ")
            self.saved_sub_input()

    def saved_sub_input(self):
        """Method to manage entries for saved or not the substitute"""
        if self.product_sub == "y":
            self.mysql.saved_product_substitute(self.product_selected,
                                                self.prod_sub)
            self.leave_saved_sub -= 1
        elif self.product_sub == "n":
            self.leave_saved_sub -= 1
        elif self.product_sub == "q":
            self.leave_saved_sub -= 1
