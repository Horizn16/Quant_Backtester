import React, { useState } from 'react';
import axios from 'axios';

function Arbit() {
  const [symbol, setSymbol] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [symbolData, setSymbolData] = useState([]);
  const [symbolBoData, setSymbolBoData] = useState([]);
  const [showTable, setShowTable] = useState(false);

  const handleSymbolClick = () => {
    setShowTable(!showTable); // Toggle the showTable state
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/arbitrage', {
        symbol,
        start_date: startDate,
        end_date: endDate
      });

      setSymbolData(response.data.symbol_data);
      setSymbolBoData(response.data.symbol_bo_data);
    } catch (error) {
      console.error('There was an error fetching the data!', error);
    }
  };

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
      <br />
      <br />
      <h4 onClick={handleSymbolClick}>{symbol}</h4>
      {showTable && (
        <>
          <h5>Symbol Data</h5>
          {symbolData.length > 0 && (
            <table>
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Close</th>
                  <th>Open</th>
                </tr>
              </thead>
              <tbody>
                {symbolData.map((row, index) => (
                  <tr key={index}>
                    <td>{row.Date}</td>
                    <td>{row.Close}</td>
                    <td>{row.Open}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
          <h5>Symbol BO Data</h5>
          {symbolBoData.length > 0 && (
            <table>
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Close</th>
                  <th>Open</th>
                </tr>
              </thead>
              <tbody>
                {symbolBoData.map((row, index) => (
                  <tr key={index}>
                    <td>{row.Date}</td>
                    <td>{row.Close}</td>
                    <td>{row.Open}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </>
      )}
    </div>
  );
}

export default Arbit;
