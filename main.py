import json
from datetime import datetime

from ingestion.alpha_vantage import get_daily_stock

symbol = "AAPL"
data = get_daily_stock(symbol)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"data/landing/alpha_vantage/stock_daily/{symbol}/{symbol}_{timestamp}.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Arquivo salvo em: {file_path}")