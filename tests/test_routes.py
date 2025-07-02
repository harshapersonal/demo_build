import unittest
from app import app

ROUTES_TO_TEST = [
    ('/', b'Welcome to the Flask API!'),
    ('/hello', b'Hello, World!'),
    # Add more routes and expected content as you add them
]

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_all_routes(self):
        for route, expected_content in ROUTES_TO_TEST:
            response = self.app.get(route)
            self.assertEqual(response.status_code, 200, f"Failed at {route}")
            self.assertIn(expected_content, response.data, f"Content check failed at {route}")

if __name__ == "__main__":
    unittest.main()
