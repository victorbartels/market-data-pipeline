create table if not exists silver.stock_prices_daily (
    id bigserial primary key,
    symbol varchar(20) not null,
    trade_date date not null,
    open_price numeric(18, 6),
    high_price numeric(18, 6),
    low_price numeric(18, 6),
    close_price numeric(18, 6),
    volume bigint,
    source varchar(100) not null,
    created_at timestamp not null default current_timestamp,

    constraint uq_stock_prices_daily unique (symbol, trade_date)
);
