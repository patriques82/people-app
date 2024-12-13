from config_tests import TestConfig

class TestPersonsView(TestConfig):
    def test_persons_route(self):
        response = self.app.get("/persons")
        print(response.data)
        self.assertEqual(response.status_code, 200)
