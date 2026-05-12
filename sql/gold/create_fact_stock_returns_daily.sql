create table if not exists gold.fact_stock_returns_daily (
    id bigserial primary key,
    symbol varchar(20) not null,
    trade_date date not null,
    close_price numeric(18, 6) not null,
    previous_close_price numeric(18, 6),
    daily_return numeric(18, 8),
    source varchar(100) not null,
    created_at timestamp not null default current_timestamp,

    constraint uq_fact_stock_returns_daily unique (symbol, trade_date)
);
