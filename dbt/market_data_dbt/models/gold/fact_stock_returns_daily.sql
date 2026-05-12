{{ config(materialized='table') }}
with stock_prices as (
    select *
    from {{ ref('silver_stock_prices') }}
),
returns as (
    select
        symbol,
        trade_date,
        close_price,
        lag(close_price) over (
            partition by symbol
            order by trade_date
        ) as previous_close_price,
        source
    from stock_prices
)
select
    symbol,
    trade_date,
    close_price,
    previous_close_price,
    (close_price - previous_close_price)
        / nullif(previous_close_price, 0) as daily_return,
    source
from returns