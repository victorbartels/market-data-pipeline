import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def load_bronze_to_silver():

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
                    insert into silver.stock_prices_daily (
                        symbol,
                        trade_date,
                        open_price,
                        high_price,
                        low_price,
                        close_price,
                        volume,
                        source
                    )
                    select
                        b.symbol,
                        b.trade_date,
                        b.open_price,
                        b.high_price,
                        b.low_price,
                        b.close_price,
                        b.volume,
                        b.source
                    from bronze.alpha_vantage_stock_daily b
                    on conflict (symbol, trade_date)
                    do nothing
                    """
                )

        print("Carga Silver concluída.")

    finally:
        conn.close()