import json
from datetime import datetime

from ingestion.alpha_vantage import get_daily_stock
from ingestion.load_raw_to_postgres import load_raw_stock_file
from ingestion.raw_to_bronze import load_raw_to_bronze
from ingestion.bronze_to_silver import load_bronze_to_silver
from ingestion.silver_to_gold import load_silver_to_gold
from ingestion.upload_to_adls import upload_file_to_adls

symbol = "AAPL"

data = get_daily_stock(symbol)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

file_path = (
    f"data/landing/alpha_vantage/stock_daily/"
    f"{symbol}/{symbol}_{timestamp}.json"
)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Arquivo salvo em: {file_path}")

load_raw_stock_file(
    file_path=file_path,
    symbol=symbol,
)

load_raw_to_bronze()
load_bronze_to_silver()
load_silver_to_gold()
upload_file_to_adls(file_path)