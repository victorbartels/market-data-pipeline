from ingestion.alpha_vantage import get_daily_stock

data = get_daily_stock("AAPL")

print(data)