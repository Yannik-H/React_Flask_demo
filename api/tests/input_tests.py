import unittest
from app import app
import json


class TestQuery(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.app.config['TESTING'] = True
        self.client = app.test_client()
        self.default_input = {"firstName": "Yuning", "lastName": "Huang", "zipCode": "02115"}

    def test_empty_first_name(self):
        self.default_input["firstName"] = ""
        json_input = json.dumps(self.default_input)
        response = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response.status_code == 400
        assert response.data.decode() == "The first name can not be empty!"

    def test_wrong_first_name(self):
        # number in the name
        self.default_input["firstName"] = "Yun1ng"
        json_input = json.dumps(self.default_input)
        response1 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response1.status_code == 400
        assert response1.data.decode() == "Please input a valid first name!"

        # illegal length
        self.default_input["firstName"] = "Yuniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiing"
        json_input = json.dumps(self.default_input)
        response2 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response2.status_code == 400
        assert response2.data.decode() == "The length of the first name can not be larger than 20!"

        # illegal symbol in the name
        self.default_input["firstName"] = "Yun!ng"
        json_input = json.dumps(self.default_input)
        response3 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response3.status_code == 400
        assert response3.data.decode() == "Please input a valid first name!"

    def test_empty_last_name(self):
        self.default_input["lastName"] = ""
        json_input = json.dumps(self.default_input)
        response = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response.status_code == 400
        assert response.data.decode() == "The last name can not be empty!"

    def test_wrong_last_name(self):
        # number in the name
        self.default_input["lastName"] = "Huan9"
        json_input = json.dumps(self.default_input)
        response1 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response1.status_code == 400
        assert response1.data.decode() == "Please input a valid last name!"

        # illegal length
        self.default_input["lastName"] = "Huanggggggggggggggggggggggggggggggggggg"
        json_input = json.dumps(self.default_input)
        response2 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response2.status_code == 400
        assert response2.data.decode() == "The length of the last name can not be larger than 20!"

        # illegal symbol in the name
        self.default_input["lastName"] = "Hu@ng"
        json_input = json.dumps(self.default_input)
        response3 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response3.status_code == 400
        assert response3.data.decode() == "Please input a valid last name!"

    def test_empty_zip_code(self):
        self.default_input["zipCode"] = ""
        json_input = json.dumps(self.default_input)
        response = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response.status_code == 400
        assert response.data.decode() == "Please input a valid zip code!"

    def test_wrong_zip_code(self):
        # letter in the name
        self.default_input["zipCode"] = "02i15"
        json_input = json.dumps(self.default_input)
        response1 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response1.status_code == 400
        assert response1.data.decode() == "Please input a valid zip code!"

        # illegal length
        self.default_input["zipCode"] = "021155"
        json_input = json.dumps(self.default_input)
        response2 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response2.status_code == 400
        assert response2.data.decode() == "Please input a valid zip code!"

        # illegal symbol in the name
        self.default_input["zipCode"] = "02!15"
        json_input = json.dumps(self.default_input)
        response3 = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response3.status_code == 400
        assert response3.data.decode() == "Please input a valid zip code!"

    def test_correct_input(self):
        self.default_input["zipCode"] = "02116"
        json_input = json.dumps(self.default_input)
        response = self.client.post("/create_phrase", content_type='application/json', data=json_input)
        assert response.status_code == 200

        data = json.loads(response.get_data())
        assert data['county'] == 'Suffolk'
        assert data['firstName'] == "Uningyay"
        assert data['lastName'] == 'uanghay'
        assert data['population'] == '28441'
