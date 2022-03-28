# Getting Started

Download and unzip the project. You can also find the project at []:[this repository](https://github.com/Yannik-H/React_Flask_demo).

### Install backend packages

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ _
$ cd ./api
$ pip install -r requirements.txt
```

### Install frontend packages

```bash
$ cd ../
$ npm install
```

### Start frontend and backend

Start two terminals:

Terminal1 to start the frontend:

```
$ yarn start
```

Terminal2 to start the backend:

```
$ yarn start-api
```

Then you should be able to see a broser window is opened at localhost:3000

### Start querying

1. Input the first name, last name and zip code, then click the submit button. A piece of message about the transformed name, county and population will be displayed in a single line above the form area, if the query is successful;
2. If you input any illegal string and submit the form, an error message will also be displayed telling you where goes wrong. The error message can be different, like `The first name can not be empty`, `Please input a valid first name!` and so on;
3. Please be careful, **do not query for more than 5 times** in an hour, because of the limitatioin of the API I used. (But you can query infinitely with zip code 02115 if you want to do some testing). If you query too much, you will found message like:`HTTP failed! Code:401 `;
4. The message denoting successful query is like: `Uningyay uanghay's zip code is in Suffolk County and has a population of 28441` with input `{first name = "Yuning", last name = "Huang", zip code = "02115"}`.

# Testing

### Frontend testing 

Note: Because of the mid-term exam this week and the workload of the course, I have little time to learn how to test frontend for interactive activities that I have no former experience before. But I write a naive test case with `enzyme` that you can find in `__test__` directory.

#### Test plans

1. Test each components can be render correctly;
2. Test the submit button and the changes of display area after clicking the button;
3. Test if error message can be correctly shown with both inputing illegal inputs and legal inputs;

### Backend testing

You can find unit tests of backend in `./api/tests/input_tests.py`.

#### Test plans

1. Test illegal inputs and corresponding error messages;
2. Test legal inputs and expected query results.



# Reference

[Zip query API]: [Zip API US - An API for performing various zip code related lookups](https://zipapi.us/)

