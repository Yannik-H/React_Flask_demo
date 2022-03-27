import React, { useState } from "react";
import { FloatingLabel, Form, Button } from "react-bootstrap";

import "./input.css";

const NewInput = (props) => {
  const [name, setName] = useState({ firstName: "", lastName: "" });
  const [zipCode, setzipCode] = useState("");

  const firstNameChangeHandler = (event) => {
    const newName = { firstName: event.target.value, lastName: name.lastName };
    setName(newName);
  };

  const lastNameChangeHandler = (event) => {
    const newName = { firstName: name.firstName, lastName: event.target.value };
    setName(newName);
  };

  const zipCodeChangeHandler = (event) => {
    setzipCode(event.target.value);
  };

  async function query (json_data) {
    const response = await fetch("/create_phrase", {
      method: "POST",
      headers: new Headers({

        "Content-Type": "application/json;charset=UTF-8",
      }),
      body: json_data,
    });
    if (!response.ok) {
      // throw new Error(response.status);
    //   console.log("Query Failed");
      console.log(response.status);
      if (response.status === 400) {
          response.text().then(errorMessage => props.errorHandler(errorMessage))
      } else {
          props.errorHandler(`HTTP failed! Code:${response.status}`);
      }
    } else {
        const res = response.json();
        res.then((data) => props.setNewInfoHandler(data));
    }
    // res.then((data) => console.log(data));
  };

  const onFormSubmit = (event) => {
    event.preventDefault();

    const json_data = JSON.stringify({
      firstName: name.firstName,
      lastName: name.lastName,
      zipCode: zipCode,
    });
    query(json_data);
  };

  return (
    <div className="input-form">
      <Form onSubmit={onFormSubmit}>
        <Form.Group>
          <FloatingLabel
            controlId="floatingInput"
            label="First Name"
            className="mb-3"
          >
            <Form.Control
              type="first_name"
              placeholder="First Name"
              value={name.firstName}
              onChange={firstNameChangeHandler}
              className="first-name-input"
            />
          </FloatingLabel>
        </Form.Group>
        <Form.Group>
          <FloatingLabel
            controlId="floatingInput"
            label="Last Name"
            className="mb-3"
          >
            <Form.Control
              type="last_name"
              placeholder="Last Name"
              value={name.lastName}
              onChange={lastNameChangeHandler}
              className="last-name-input"
            />
          </FloatingLabel>
        </Form.Group>
        <Form.Group>
          <FloatingLabel
            controlId="floatingInput"
            label="Zip Code"
            className="mb-3"
          >
            <Form.Control
              type="zip_code"
              placeholder="Zip Code"
              value={zipCode}
              onChange={zipCodeChangeHandler}
              className="zip-Code-input"
            />
          </FloatingLabel>
        </Form.Group>

        <Button variant="primary" type="submit" className="submit-button">
          Submit
        </Button>
      </Form>
    </div>
  );
};

export default NewInput;
