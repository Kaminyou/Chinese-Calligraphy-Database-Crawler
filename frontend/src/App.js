import React, { useState } from "react";
import './App.css';
import logo from './word.png'
import { word2idx } from "./data"

import { TextField, Button } from "@material-ui/core";


function App() {
  
  const [word, setWord] = useState("");
  const [url, setUrl] = useState("");
  const [urlword, setUrlWord] = useState("");

  const inputOnChange = (e) => {
    setWord(e.target.value)
  }

  const searchOnClick = () => {
    if (word.length > 1) {
      alert("僅能輸入一個字!");
      return;
    } 
    if (word.length === 0) {
      alert("請輸入一個中文字!");
      return;
    }
    let result = word2idx[word];
    if (result === undefined) {
      alert("無此法帖!");
      return;
    }
    setUrl("https://www.cns11643.gov.tw/wordWrite.jsp?ID=" + result);
    setUrlWord(word);
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} width="100px"></img>
        <h1>全字庫法帖查詢</h1>
        <div>
          <TextField id="standard-basic" label="中文字" variant="standard" onChange={inputOnChange}/>
          <Button variant="contained" onClick={searchOnClick}>Search</Button>
        </div>
          <p>Link: <a href={url} target="_blank" rel="noreferrer">{urlword}</a></p>
        
      </header>
    </div>
  );
}

export default App;
