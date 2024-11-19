import React, { useState } from 'react';
import axios from 'axios';

function Nifty() {
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [data, setData] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/nifty_stock', {
        start_date: startDate,
        end_date: endDate
      });
      setData(response.data);
    } catch (error) {
      console.error('There was an error fetching the data!', error);
    }
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Start Date:
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
        </label>
        <br />
        <label>
          End Date:
          <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
        </label>
        <br />
        <button type="submit" className="btn btn-primary">Fetch Data</button>
      </form>
      {data.length > 0 && (
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
            {data.map((row, index) => (
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
        
  {data.map((row, index) => (
<h1 key={index}>{row.Cumulative_Return}</h1>
  ))}
    </div>
  )
}

export default Nifty
