// src/App.js
import React, { useState } from 'react';

import NewInput from './components/inputForm/input';
import ResultDisplay from './components/resultDisplay/result';

import './App.css';

function App() {

  const [currentDisplay, setDisplay] = useState("Your query result will be shown here!");

  const setNewInfoHandler = (newInfo) => {
    let newDisplay = "Your query result will be shown here!";
    if (!newInfo) {
      newDisplay = "Query Failed! Please try again later!";
    } else {
      newDisplay = `${newInfo.firstName} ${newInfo.lastName}'s zip code is in ${newInfo.county} County and has a population of ${newInfo.population}`;
    }
    setDisplay(newDisplay);
  }

  const errorHandler = (errorMessage) => {
    setDisplay(errorMessage);
  }

  return (
    <div>
      <header className="App-header">
        <div className='query-result'>
          <ResultDisplay content={currentDisplay}/>
        </div>
        <div className='info-search'>
          <NewInput setNewInfoHandler={setNewInfoHandler} errorHandler={errorHandler}/>
        </div>
      </header>
    </div>
  );
}

export default App;