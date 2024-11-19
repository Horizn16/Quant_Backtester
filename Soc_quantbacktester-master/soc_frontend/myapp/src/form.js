import React, { useState } from 'react';
import axios from 'axios';
import Nifty from './nifty';
import {Chart as ChartJS} from "chart.js/auto";
import {Line} from"react-chartjs-2";

import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
function StockForm() {
  const [symbol, setSymbol] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [data, setData] = useState([]);
  const [data2, setData2] = useState([]);
  const [Xlabel , setXlabel]  = useState('')
  const [showTable, setShowTable] = useState(false);

  const handleSymbolClick = () => {
    setShowTable(!showTable); // Toggle the showTable state
  };
  const [showTable2, setShowTable2] = useState(false);

  const handleSymbolClick2 = () => {
    setShowTable2(!showTable2); // Toggle the showTable state
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/get_stock_data', {
        symbol,
        start_date: startDate,
        end_date: endDate
      });

      setData(response.data);
      const response2 = await axios.post('http://127.0.0.1:5000/nifty_stock', {
        start_date: startDate,
        end_date: endDate
      });
      setData2(response2.data);
    } catch (error) {
      console.error('There was an error fetching the data!', error);
    }
  };

  const createChartData = (label, dataSet, color ,) => ({
    labels: dataSet.map(row => row.Date),
    datasets: [
      {
        label: label,
        data: dataSet.map(row => row.cumulative_return),
        borderColor: color,
        fill: false,
      },
    ],
  });

  return (
    <div>
<form onSubmit={handleSubmit} className="container mt-4">
  <div className="form-row align-items-center">
    <div className="col-auto">
      <label className="sr-only" htmlFor="symbolInput">Symbol</label>
      <input 
        type="text" 
        className="form-control mb-2" 
        id="symbolInput" 
        placeholder="Symbol"
        value={symbol} 
        onChange={(e) => setSymbol(e.target.value)} 
      />
    </div>
    <div className="col-auto">
      <label className="sr-only" htmlFor="startDateInput">Start Date</label>
      <input 
        type="date" 
        className="form-control mb-2" 
        id="startDateInput" 
        value={startDate} 
        onChange={(e) => setStartDate(e.target.value)} 
      />
    </div>
    <div className="col-auto">
      <label className="sr-only" htmlFor="endDateInput">End Date</label>
      <input 
        type="date" 
        className="form-control mb-2" 
        id="endDateInput" 
        value={endDate} 
        onChange={(e) => setEndDate(e.target.value)} 
      />
    </div>
    <div className="col-auto">
      <button type="submit" className="btn btn-primary mb-2">Fetch Data</button>
    </div>
  </div>
</form>


      <br/>
      <h4 onClick={handleSymbolClick}>{symbol}</h4>
      {showTable && data.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Close</th>
              <th>Open</th>
              <th>High</th>
              <th>Low</th>
              <th>Volume</th>
              <th> Daily return</th>
              
              <th> net cumulative return </th>
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={index}>
                <td>{row.Date}</td>
                <td>{row.Close}</td>
                <td>{row.Open}</td>
                <td>{row.High}</td>
                <td>{row.Low}</td>
                <td>{row.Volume}</td>
                <td>{row.Daily_Return}</td>
                <td>{row.cumulative_return}</td>
              </tr>
              
            ))}
          </tbody>
        </table>
        )}
        
{data.length >0 &&( 
        <h4 onClick={handleSymbolClick2}>Nifty 50</h4>
)}{showTable2 && data2.length > 0 && (

         
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Close</th>
              <th>Open</th>
              <th>High</th>
              <th>Low</th>
              <th>Volume</th>
            
              <th> net cumulative return </th>
            </tr>
          </thead>
          <tbody>
            {data2.map((row, index) => (
              <tr key={index}>
                <td>{row.Date}</td>
                <td>{row.Close}</td>
                <td>{row.Open}</td>
                <td>{row.High}</td>
                <td>{row.Low}</td>
                <td>{row.Volume}</td>
                <td>{row.cumulative_return}</td>
              </tr>
              
            ))}
          </tbody>
        </table>
        )}
    {data.length > 0 && data2.length > 0 && (
  <div>
    <h4> Returns:</h4>
    <table>
      <thead> <tr>
      <th>
        {symbol}
      </th>
      <th>
        Nifty 50
      </th>
    </tr></thead>
   <tbody> <tr>
      <td>{data[data.length - 1].cumulative_return}</td>
    <td>{data2[data2.length - 1].cumulative_return}
    </td>
    </tr></tbody>
   
    </table>
  </div>
)}
<Link to="/edit">Move to trading</Link>

{data.length > 0 && (
        <Line
          data={createChartData(symbol, data, 'rgb(0, 217,255)' ) }
        />
      )}

      {data2.length > 0 && (
        <Line
          data={createChartData('Nifty 50', data2, 'rgb(255,0,0)')}
        />
      )}
    </div>
  );
}

export default StockForm;

