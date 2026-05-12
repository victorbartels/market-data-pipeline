{{ config(materialized='table') }}
with raw_data as (
    select
        id as raw_id,
        symbol,
        source,
        ingestion_timestamp,
        raw_json
    from raw.alpha_vantage_stock_daily_raw
),
daily_series as (
    select
        raw_id,
        symbol,
        source,
        ingestion_timestamp,
        jsonb_each(raw_json -> 'Time Series (Daily)') as daily_data
    from raw_data
)
select
    raw_id,
    symbol,
    source,
    ingestion_timestamp,
    (daily_data).key::date as trade_date,
    ((daily_data).value ->> '1. open')::numeric as open_price,
    ((daily_data).value ->> '2. high')::numeric as high_price,
    ((daily_data).value ->> '3. low')::numeric as low_price,
    ((daily_data).value ->> '4. close')::numeric as close_price,
    ((daily_data).value ->> '6. volume')::bigint as volume
from daily_series