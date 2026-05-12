import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def load_raw_to_bronze():
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
                    select
                        id,
                        symbol,
                        source,
                        ingestion_timestamp,
                        raw_json
                    from raw.alpha_vantage_stock_daily_raw
                    order by id
                    """
                )

                raw_rows = cursor.fetchall()

                for row in raw_rows:

                    raw_id = row[0]
                    symbol = row[1]
                    source = row[2]
                    ingestion_timestamp = row[3]
                    raw_json = row[4]

                    time_series = raw_json.get("Time Series (Daily)", {})

                    for trade_date, values in time_series.items():

                        cursor.execute(
                            """
                            insert into bronze.alpha_vantage_stock_daily (
                                raw_id,
                                symbol,
                                trade_date,
                                open_price,
                                high_price,
                                low_price,
                                close_price,
                                volume,
                                source,
                                ingestion_timestamp
                            )
                            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            (
                                raw_id,
                                symbol,
                                trade_date,
                                values.get("1. open"),
                                values.get("2. high"),
                                values.get("3. low"),
                                values.get("4. close"),
                                values.get("5. volume"),
                                source,
                                ingestion_timestamp,
                            ),
                        )

        print("Carga Bronze concluída.")

    finally:
        conn.close()