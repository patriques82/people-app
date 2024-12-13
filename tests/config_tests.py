import sqlite3
import unittest
from unittest.mock import patch

from app import app

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        cursor = self.connection.cursor()

        cursor.execute(""" 
            CREATE TABLE People (
	            ID INTEGER PRIMARY KEY,
	            FirstName TEXT NOT NULL,
	            LastName TEXT,
                Age INTEGER
            );
        """)
        cursor.execute("""
           INSERT INTO People (FirstName, LastName, Age)
           VALUES ("Astrid", "Lindgren", 88);          
        """)
        self.connection.commit()

        self.db_connection_patch = patch("app.db_connection", return_value=self.connection)
        self.db_connection_patch.start()
        
        self.app = app.test_client()

    def tearDown(self):
        self.connection.close()