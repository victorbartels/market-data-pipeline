create table if not exists bronze.alpha_vantage_stock_daily (
    id bigserial primary key,
    raw_id bigint not null,
    symbol varchar(20) not null,
    trade_date date not null,
    open_price numeric(18, 6),
    high_price numeric(18, 6),
    low_price numeric(18, 6),
    close_price numeric(18, 6),
    adjusted_close_price numeric(18, 6),
    volume bigint,
    source varchar(100) not null,
    ingestion_timestamp timestamp not null,
    created_at timestamp not null default current_timestamp
);
