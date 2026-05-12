import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def load_silver_to_gold():
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
                    insert into gold.fact_stock_returns_daily (
                        symbol,
                        trade_date,
                        close_price,
                        previous_close_price,
                        daily_return,
                        source
                    )
                    select
                        symbol,
                        trade_date,
                        close_price,
                        lag(close_price) over (
                            partition by symbol
                            order by trade_date
                        ) as previous_close_price,
                        (
                            close_price - lag(close_price) over (
                                partition by symbol
                                order by trade_date
                            )
                        ) / nullif(
                            lag(close_price) over (
                                partition by symbol
                                order by trade_date
                            ),
                            0
                        ) as daily_return,
                        source
                    from silver.stock_prices_daily
                    on conflict (symbol, trade_date)
                    do nothing
                    """
                )

        print("Carga Gold concluída.")

    finally:
        conn.close()