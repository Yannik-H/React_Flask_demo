import React from "react";

import "./result.css"

const ResultDisplay = props => {
    return (
       <div className="display-area">
           <h3 className="result-content">{props.content}</h3>
       </div>
    );

}

export default ResultDisplay;