from stockdata import StockData
from regression import LinearRegression


if __name__ == "__main__":
    sd = StockData()
    cv = sd.get_stocks('TSLA', 'TIME_SERIES_DAILY_ADJUSTED', 10)
