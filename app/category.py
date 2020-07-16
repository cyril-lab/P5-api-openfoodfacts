#!/usr/bin/python3
# -*- coding: Utf-8 -*

from app.database import Database
from config import config


class Category(Database):
    """This class allows to communicate with the category table"""

    def save_category(self):
        """Method to save the categories in the database"""
        self.start_connection()
        for element in config.CATEGORIES:
            self.cursor.execute(f"""
                INSERT INTO category (name) VALUES ("{element}")""")
        self.mysql_connection.commit()
        self.close_connection()
