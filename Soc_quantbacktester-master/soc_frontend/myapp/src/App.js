import logo from './logo.svg';
import './App.css';
import form from './form';
import Form from './form';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import StockForm from './form';
import { BrowserRouter as Router, Routes, Route, Switch, Link, BrowserRouter } from 'react-router-dom';
import Nifty from './nifty';
import Edit from './editor';
import Trend from './trend';
import Arbit from './arbitage';

function App() {
  const [data, setData] = useState(null);

  

  return (
    
    <BrowserRouter>
    <div className="App">
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    <a className="navbar-brand" href="/">Stock Data</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="/">Show Data</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/edit">Editor</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/arbit">INDEXES</a>
        </li>
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="/trend">Trend</a>
        </li>
        <li className="nav-item">
          <a className="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
    <header className="App-header"></header>
    <Routes>
    <Route path="/" element={<StockForm/>} />
    {/* <Route path='/' element={<StockForm/>}> */}
    <Route path="/edit" element={<Edit/>} />
    {/* <Route path="/arbit" element={<Arbit/>} /> */}
    <Route path="/trend" element={<Trend/>} />
    {/* </Route> */}
    </Routes>

      {/* <StockForm/> */}
  </div>
  </BrowserRouter>
  );
}


export default App;
