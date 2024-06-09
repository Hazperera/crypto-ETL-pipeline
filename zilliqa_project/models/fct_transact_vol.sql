-- models/fct_transact_vol.sql

-- Transaction Volume

SELECT
  DATE_TRUNC(block_timestamp, DAY) AS day,
  COUNT(*) AS transaction_count
FROM
  `datafella-workbook.dbt_hp.dim_transactions`
GROUP BY
  day
ORDER BY
  day


