import React, { useState } from 'react';
import axios from 'axios';
import { Chart as ChartJS } from 'chart.js/auto';
import { Line } from 'react-chartjs-2';

function Trend() {
  const [symbol, setSymbol] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [data, setData] = useState([]);
  const [chartData, setChartData] = useState({});
  const [showTable, setShowTable] = useState(false);

  const handleSymbolClick = () => {
    setShowTable(!showTable); // Toggle the showTable state
  };
  

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/stock_trend', {
        symbol,
        start_date: startDate,
        end_date: endDate
      });

      setData(response.data);
      prepareChartData(response.data);
    } catch (error) {
      console.error('There was an error fetching the data!', error);
    }
  };

  const prepareChartData = (data) => {
    const dates = data.map(row => row.Date);
    const closes = data.map(row => row.Close);
    const macds = data.map(row => row.MACD);
    const macdSignals = data.map(row => row.MACD_Signal);

    setChartData({
      labels: dates,
      datasets: [
        {
          label: 'Close Price',
          data: closes,
          borderColor: 'blue',
          borderWidth: 1,
          yAxisID: 'y',
        },
        {
          label: 'MACD',
          data: macds,
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
          yAxisID: 'y1',
        },
        {
          label: 'MACD Signal',
          data: macdSignals,
        
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
          yAxisID: 'y2',
        }
      ],
    });
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
      <br/>
      <h4 onClick={handleSymbolClick}>{symbol}</h4>
      { showTable &&  data.length > 0 && (
        <>
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Close</th>
                <th>Open</th>
                <th>SMA_9</th>
                <th>SMA_20</th>
                <th>MACD</th>
                <th>MACD Signal</th>
                {/* <th>cumulative_return</th> */}
              </tr>
            </thead>
            <tbody>
              {data.map((row, index) => (
                <tr key={index}>
                  <td>{row.Date}</td>
                  <td>{row.Close}</td>
                  <td>{row.Open}</td>
                  <td>{row.SMA_9}</td>
                  <td>{row.SMA_20}</td>
                  <td>{row.MACD}</td>
                  <td>{row.MACD_Signal}</td>
              
                  {/* <td>{row.cumulative_return}</td> */}
                </tr>
              ))}
            </tbody>
          </table>
          <Line
        data={chartData}
        options={{
          scales: {
            y: {
              type: 'linear',
              display: true,
              position: 'left',
            },
            y1: {
              type: 'linear',
              display: true,
              position: 'right',
            },
            y2: {
              type: 'linear',
              display: true,
              position: 'right',
            },
          },
        }}
      />
          
        </>
      )}
      
    </div>
  );
}


export default Trend;
