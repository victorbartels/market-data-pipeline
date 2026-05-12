import json
import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def load_raw_stock_file(file_path: str, symbol: str) -> None:
    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    insert into raw.alpha_vantage_stock_daily_raw (
                        symbol,
                        source,
                        file_name,
                        raw_json
                    )
                    values (%s, %s, %s, %s::jsonb)
                    """,
                    (
                        symbol,
                        "alpha_vantage",
                        path.name,
                        json.dumps(raw_data),
                    ),
                )

        print(f"Arquivo carregado na raw: {path.name}")

    finally:
        conn.close()