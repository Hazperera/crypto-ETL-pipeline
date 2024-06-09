-- models/dim_transactions.sql

-- Core Transaction Details and Status

SELECT
  id,
  block_number,
  block_timestamp,
  amount,
  code,
  data,
  version,
  accepted,
  success,
  epoch_num
FROM
  `bigquery-public-data.crypto_zilliqa.transactions`
