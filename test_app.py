"""Unit tests for the Flask application."""

import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    """Test cases for Flask application."""

    def setUp(self):
        """Setup test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test home route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"1RVU23CSE019", response.data)

if __name__ == '__main__':
    unittest.main()
