import yfinance as yf
import matplotlib.pyplot as plt

def stock_analysis():
    # Download stock data for Apple (AAPL)
    data = yf.download('AAPL', start='2020-01-01', end='2022-12-31', auto_adjust=True)

    # Calculate moving averages
    data['20-day MA'] = data['Close'].rolling(window=20).mean()
    data['50-day MA'] = data['Close'].rolling(window=50).mean()
    
    # Plotting the close price and moving averages
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='AAPL Close Price', color='blue')
    plt.plot(data.index, data['20-day MA'], label='20-Day Moving Average', color='orange')
    plt.plot(data.index, data['50-day MA'], label='50-Day Moving Average', color='green')
    
    plt.title('AAPL Stock Price & Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)
    
    # Save the plot as an image file
    plt.savefig('stock_analysis.png')  # Save file in current directory
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    stock_analysis()
