#!/usr/bin/python3
# -*- coding: Utf-8 -*

from cleardata import ClearData
from database import Database
import config


class Application:

    def __init__(self):
        self.mysql = Database("localhost", "cyril", "qsdf678/", "p5" )
        self.category = ""
        self.products = []
        self.products_sub = []
        self.product_selected = []
        self.prod_sub = []
        
    def main(self):
        self.main_menu()

    def initialise_bdd(self):
        self.mysql.create_database("p5.sql")
        self.mysql.saved_category()

    def saved_product_bdd(self):
        for element in config.CATEGORIES:
            category = ClearData(element)
            category.get_data_api()
            category.generate_products_list()
            self.mysql.saved_product(category.products, config.CATEGORIES.index(element)+1)

    def main_menu(self):
        leave_main_menu = 1
        while leave_main_menu :
            print("\n 1 : Choisir une catégorie. \n 2 : Afficher les substituts. \n 3 : Réinitialiser BDD. \n 4 : Quitter le programme.")
            choice = input("\n Veuillez saisir votre choix : ")
            if choice == "1" :
                self.category_choice()
            elif choice == "2" :
                print("\n Produit origine / produit de substitution :\n")
                for element in self.mysql.get_substitution():
                    for substitution in element:
                        test = self.mysql.get_product(substitution)
                        print(test[0][1]+" - "+test[0][2]+" - "+test[0][3]+" - "+test[0][4])
                    print("     ")
            elif choice == "3" :
                self.initialise_bdd()
                self.saved_product_bdd()
            elif choice == "4" :
                leave_main_menu -= 1

    def category_choice(self):
        leave = 1
        while leave:
            print("\n Catégories :\n")
            for element in config.CATEGORIES:
                    print(str(config.CATEGORIES.index(element)+1)+" : "+element)
            try:        
                self.category =  input("\n Veuillez saisir votre choix : ")
                if self.category == "q":
                    leave -= 1
                elif 1 <= int(self.category) <= len(config.CATEGORIES):
                    print(self.category)
                    self.products = self.mysql.get_list_product(self.category)
                    self.products_sub = self.mysql.get_list_product(self.category)
                    self.choise_product()
                    leave -= 1
            except :
                print("\n Saisie incorrecte")    


    def choise_product(self):
        first_number = 0
        leave = 1
        while leave:
            print("\n Choisissez un produit à remplacer : \n")
            for element in self.products[first_number:first_number + config.NUMBER_PRODUCT_DISPLAY]:
                print(str(self.products.index(element)+1)+" - "+ element[1] +" - "+ element[4].upper())
            input_produit = input("\n Entrez votre choix (s/suivant, p/précédent): ")

            try:
                if input_produit == "s" and (first_number + config.NUMBER_PRODUCT_DISPLAY) < len(self.products):
                    first_number += config.NUMBER_PRODUCT_DISPLAY
                elif input_produit =="p" and first_number > 0:
                    first_number -= config.NUMBER_PRODUCT_DISPLAY
                elif input_produit =="q":
                    leave -=1
                elif 1 <= int(input_produit) <= len(self.products): 
                    self.product_selected = self.products[int(input_produit)-1][0]
                    del self.products_sub[int(input_produit)-1]
                    self.choise_sub()
                    leave -=1
            except:
                print("Saisie incorrecte")    

    def choise_sub(self):
        first_number1 = 0
        leave = 1
        while leave:
            print("\n Choisissez un produit de substitution : \n")
            for element in self.products_sub[first_number1:first_number1+ config.NUMBER_PRODUCT_DISPLAY]:
                print(str(self.products_sub.index(element)+1)+" - "+ element[1] +" - "+ element[4].upper())
            input_produit_sub = input("\n Entrez votre choix (s/suivant, p/précédent): ")

            try:
                if input_produit_sub == "s" and (first_number1 + config.NUMBER_PRODUCT_DISPLAY) < len(self.products_sub):
                    first_number1 += 5
                elif input_produit_sub =="p" and first_number1 > 0:
                    first_number1 -= 5
                elif input_produit_sub =="q":
                    leave -=1
                elif 1 <= int(input_produit_sub) <= len(self.products_sub): 
                    self.prod_sub = self.products_sub[int(input_produit_sub)-1][0]
                    self.saved_sub()
                    leave -=1
            except:
                print("Saisie incorrecte")        
           
    def saved_sub(self):
        leave = 1
        while leave:
            print(f"\n Voulez vous enregistrer le produit ?  id produit {self.product_selected}, id produit sub : {self.prod_sub}, :")
            produit_sub = input("y / n : ")

            try:
                if produit_sub == "y":
                    self.mysql.saved_product_substitution(self.product_selected, self.prod_sub)
                    leave -=1
                elif produit_sub == "n":
                    leave -=1
                elif produit_sub == "q":
                    leave -=1
            except:
                print("Saisie incorrecte")


if __name__ == '__main__':
    application = Application()
    application.main()


