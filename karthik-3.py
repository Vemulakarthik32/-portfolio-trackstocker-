import yfinance as yf
import pandas as pd

# Function to fetch stock data
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Adj Close']

# Function to calculate portfolio value
def calculate_portfolio_value(portfolio, prices):
    return sum(portfolio[ticker] * prices[ticker] for ticker in portfolio)

# Main function
def main():
    # Define your portfolio
    portfolio = {
        'AAPL': 10,   # Example: 10 shares of Apple
        'MSFT': 5,    # Example: 5 shares of Microsoft
        'GOOG': 3     # Example: 3 shares of Google
    }

    # Define date range
    start_date = '2023-01-01'
    end_date = '2024-01-01'

    # Fetch stock data
    prices = {}
    for ticker in portfolio.keys():
        prices[ticker] = get_stock_data(ticker, start_date, end_date)

    # Combine stock data into a DataFrame
    portfolio_value = pd.DataFrame(prices)

    # Calculate portfolio value
    portfolio_value['Portfolio Value'] = portfolio_value.apply(lambda row: calculate_portfolio_value(portfolio, row), axis=1)

    # Print portfolio value
    print(portfolio_value)

if __name__ == "__main__":
    main()
