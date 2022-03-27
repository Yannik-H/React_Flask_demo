import React from "react";
// import { render, fireEvent } from "@testing-library/react";
import { mount, shallow, configure } from 'enzyme';
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
    // console.log(wrapper.html());
    expect(wrapper.find(".first-name-input").exists());
    expect(wrapper.find(".last-name-input").exists());
    expect(wrapper.find(".zip-code-input").exists());
  });

  // test("wrong first name", () => {
  //   const wrapper = setup();
  //   const displayArea = wrapper.find(".result-content");
  //   // const test = wrapper.find("button");
  //   // console.log(test.debug());
  //   // console.log(wrapper.find("form").debug());
  //   wrapper.find("form").simulate('submit');
  //   wrapper.update();
  //   console.log(wrapper.find(".result-content").text());
  //   console.log(wrapper.debug());
  //   wrapper.find(".first-name-input").simulate("change", {target: {value: ""}})
  // })

  // test("wrong last name", () => {
  //   const wrapper = setup();
  // })

  // test("wrong zip code", () => {
  //   const wrapper = setup();
  // })

  // test("correct query", () => {
  //   const wrapper = setup();
  // })
})