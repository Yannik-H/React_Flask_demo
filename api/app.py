import json
import re

import requests
from flask import Flask, request, make_response
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

ZIP_USER_EMAIL = "huang.yuni@northeastern.edu"
ZIP_USER_PASSWORD = "Aa1123."
ZIP_API_KEY = "fdec2d285757152669482a0a12b1cd5f"

mock_database = {"02115": ["Suffolk", "28441"]}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/create_phrase', methods=['POST'])
def data_handler():
    # data = json.loads(request.get_data())
    # temp = request.json.get("firstName")
    user_input = dict(
        first_name=request.json["firstName"],
        last_name=request.json["lastName"],
        zip_code=request.json["zipCode"]
    )

    data_validation(user_input)

    pig_latin_first_name, pig_latin_last_name = pigLatinTransformer(user_input["first_name"], user_input["last_name"])
    zipcode = user_input["zip_code"]
    if zipcode == "02115":
        county = mock_database["02115"][0]
        population = mock_database["02115"][1]
    else:
        population_req = requests.get(
            "https://service.zipapi.us/zipcode/{0}?X-API-KEY={1}&fields=geolocation,population".format(zipcode,
                                                                                                       ZIP_API_KEY),
            auth=HTTPBasicAuth(ZIP_USER_EMAIL, ZIP_USER_PASSWORD))
        county_req = requests.get(
            "https://service.zipapi.us/zipcode/county/{0}?X-API-KEY={1}".format(zipcode, ZIP_API_KEY),
            auth=HTTPBasicAuth(ZIP_USER_EMAIL, ZIP_USER_PASSWORD))
        if population_req.status_code == 401:
            raise InvalidInput("Zip API exceeded hourly limit", status_code=401)
        population = json.loads(population_req.content)["data"]["population"]
        county = json.loads(county_req.content)["data"]["county"][0]

    content = {"firstName": pig_latin_first_name,
               "lastName": pig_latin_last_name,
               "county": county,
               "population": population
               }

    return content


def data_validation(user_input: dict):
    assert "first_name" in user_input
    assert "last_name" in user_input
    assert "zip_code" in user_input

    if len(user_input["first_name"]) == 0:
        raise InvalidInput("The first name can not be empty!", status_code=400)

    if len(user_input["last_name"]) == 0:
        raise InvalidInput("The last name can not be empty!", status_code=400)

    if len(user_input["first_name"]) >= 20:
        raise InvalidInput("The length of the first name can not be larger than 20!", status_code=400)

    if len(user_input["last_name"]) >= 20:
        raise InvalidInput("The length of the last name can not be larger than 20!", status_code=400)

    if not user_input["first_name"].isalpha():
        raise InvalidInput("Please input a valid first name!", status_code=400)

    if not user_input["last_name"].isalpha():
        raise InvalidInput("Please input a valid last name!", status_code=400)

    # Check the format of the zip code
    if not re.match("^[0-9]{5}(?:-[0-9]{4})?$", user_input["zip_code"]):
        raise InvalidInput("Please input a valid zip code!", status_code=400)


class InvalidInput(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code


@app.errorhandler(InvalidInput)
def invalid_usage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response


def pigLatinTransformer(first: str, last: str) -> (str, str):
    f_name = first[1:] + first[0]
    f_name = f_name.capitalize()
    f_name += "ay"
    l_name = last[1:] + last[0]
    l_name = l_name.lower()
    l_name += "ay"

    return f_name, l_name


if __name__ == '__main__':
    app.run(debug=True)


