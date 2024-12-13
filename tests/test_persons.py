from config_tests import TestConfig

class TestPersonsView(TestConfig):
    def test_persons_route(self):
        response = self.app.get("/persons")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "<li>Astrid, Lindgren age: 88</li>", 
            response.data.decode("utf-8")
        )

    def test_create_person_get_route(self):
        response = self.app.get("/createPerson")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<input type="text" name="last-name" placeholder="last name" />',
            response.data.decode("utf-8")
        )

    def test_create_person_post_route(self):
        response = self.app.post("/createPerson", data={
            "first-name": "Göran",
            "last-name": "Tunström",
            "age": 77
        })
        self.assertEqual(response.status_code, 302)
        
        response = self.app.get("/persons")
        self.assertIn(
            "<li>Göran, Tunström age: 77</li>", 
            response.data.decode("utf-8")
        )