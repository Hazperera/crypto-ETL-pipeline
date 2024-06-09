-- models/dim_transactions_gas.sql

SELECT
  id,
  gas_limit,
  gas_price,
  cumulative_gas
FROM
  `bigquery-public-data.crypto_zilliqa.transactions`
