import unittest
from app import Handler

class TestApplication(unittest.TestCase):
    def test_handler_exists(self):
        self.assertTrue(callable(Handler.do_GET))

if __name__ == "__main__":
    unittest.main()
