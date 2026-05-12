create table if not exists raw.alpha_vantage_stock_daily_raw (
    id bigserial primary key,
    symbol varchar(20) not null,
    source varchar(100) not null,
    ingestion_timestamp timestamp not null default current_timestamp,
    file_name varchar(255),
    raw_json jsonb not null
);
