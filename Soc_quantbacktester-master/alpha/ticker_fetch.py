import requests
from bs4 import BeautifulSoup
# through this code i fetch multiple tickers from yahoo finance 

def get_nse_tickers():
    url = "https://finance.yahoo.com/quote/%5ENSEI/components/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }  # User-Agent header to mimic a web browser
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table containing the components
        table = soup.find('table', class_='expandable-table')
        
        tickers = []
        if table:
            # Iterate through rows of the table skipping the first row (header)
            rows = table.find_all('tr')[1:]  # Skip header row
            for row in rows:
                # Extract ticker symbol from each row
                ticker = row.find_all('td')[0].text.strip()
                tickers.append(ticker)
        
        return tickers
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# Example usage:
# tickers = get_nse_tickers()
# print(tickers)