{{ config(materialized='table') }}
with stock_prices as (
    select *
    from {{ ref('stg_stock_prices') }}
),
deduplicated as (
    select
        symbol,
        trade_date,
        open_price,
        high_price,
        low_price,
        close_price,
        volume,
        source,
        ingestion_timestamp,
        row_number() over (
            partition by symbol, trade_date
            order by ingestion_timestamp desc
        ) as row_num
    from stock_prices
)
select
    symbol,
    trade_date,
    open_price,
    high_price,
    low_price,
    close_price,
    volume,
    source,
    ingestion_timestamp
from deduplicated
where row_num = 1