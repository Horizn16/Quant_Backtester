## Quant Backtester

This project implements a quantitative trading simulation framework using Python, and FastAPI for the web interface, and integrates HTML/CSS for visualization. It consists of three main components: Data Pre-processing, Trading Execution, and Post-Trade Analysis.

### 1. Data Pre-processing
The Data Pre-processing module is responsible for preparing and cleaning the input data to ensure it is in the proper format for trading simulations. This includes:

- Fetching and cleaning historical financial data
- Handling missing data and ensuring data consistency
- Generating statistics and summaries of the dataset 

### 2. Trading Execution
The Trading Execution component handles the actual execution of trading strategies based on the pre-processed data. Key features include:

- Implementation of various trading strategies (e.g., moving average crossover, mean reversion)
- Simulation of trades based on historical data
- Integration with external APIs for real-time data retrieval (optional).

### 3. Post-Trade Analysis
After executing a trading strategy, the Post-Trade Analysis module analyzes the results to evaluate the strategy's performance. This includes:

- Calculation of performance metrics such as Sharpe ratio, Sortino ratio, and maximum drawdown
- Visualization of results through charts and graphs (e.g., cumulative returns, monthly returns heatmap)
- Comparison against benchmark indices (e.g., Nifty index) for performance assessment

## Web Interface Development:
Built a user-friendly web interface using FastAPI:
Integrated input forms for specifying ticker name, start date, and end date.
Implemented pages for data preprocessing, strategy scripting, and post-trade analysis visualization.
Utilized HTML and CSS for frontend design, facilitating interactive strategy scripting and result visualization.

## Technologies Used:
Languages and Libraries: Python, Pandas, Matplotlib, HTML, CSS.
Frameworks: FastAPI for backend development and API integration.
