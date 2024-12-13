import unittest
from app import app

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()