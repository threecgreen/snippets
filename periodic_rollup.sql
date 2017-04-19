-- postgrSQL
/*
Create a materialized view that summarizes columns on a time period basis ie average stock
prices over 15 minute periods.
 */
CREATE MATERIALIZED VIEW prices_rollup AS
  SELECT
    stock_ticker,
    -- Break apart dates and then join them together before casting to timestamp
    (date_part('year', datetime) || '-' || date_part('month', datetime) || '-' || date_part('day', datetime) || ' '
    -- Divide by 15 (or whatever the time period) and then multiply by 15
     || date_part('hour', datetime) || ':' || 15 * div(date_part('minute', datetime), 15) || ':00')::TIMESTAMP AS rollup_timestamp,
    avg(stock_price)
  FROM stock_prices
  GROUP BY
    stock_ticker,
    -- Repete composite date
    (date_part('year', datetime) || '-' || date_part('month', datetime) || '-' || date_part('day', datetime) || ' '
     || date_part('hour', datetime) || ':' || 15 * div(date_part('minute', datetime), 15) || ':00');
