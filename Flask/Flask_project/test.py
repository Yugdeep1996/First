from app import app
import unittest

class Test_routes(unittest.TestCase):

    # Check for response 200
    def test_ifsc_search(self):
        client = app.test_client(self)
        response = client.get('/ifsc_search')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    # Check for response 200
    # Check id data returned is application/json
    def test_bank_leader_board(self):
        client = app.test_client(self)
        response = client.get('/bank_leader_board?sortorder=ASC&fetchcount=10')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    # Check for response 200
    def test_stats(self):
        client = app.test_client(self)
        response = client.get('/stats?sortorder=ASC&fetchcount=10')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")

if __name__ == "__main__":
    unittest.main()