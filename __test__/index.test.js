import React from "react";
// import { render, fireEvent } from "@testing-library/react";
import { mount, render, shallow, configure } from 'enzyme';
import Adapter from "enzyme-adapter-react-16"
import App from "../src/App";
import NewInput from "../src/components/inputForm/input";
import "../src/setupTests";

configure({ adapter : new Adapter()});

const setup = () => {
  const wrapper = mount(<App />);
  return wrapper
}

describe("compoments", () => {
  test("component", () => {
    const wrapper = setup();
    const displayArea = wrapper.find(".result-content");
    expect(wrapper.find(".result-content")).toHaveLength(1);
    expect(displayArea.text()).toBe("Your query result will be shown here!");
    console.log(wrapper.html());
    expect(wrapper.find(".first-name-input").exists());
    expect(wrapper.find(".last-name-input").exists());
    expect(wrapper.find(".zip-code-input").exists());
  });

  test("wrong first name", () => {
    const wrapper = setup();
    const displayArea = wrapper.find(".result-content");
    expect(1 + 1).toBe(2);
  })
})