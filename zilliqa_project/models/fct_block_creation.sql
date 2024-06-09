-- models/fact_block_creation.sql

WITH ds_blocks_metrics AS (
  SELECT
    DATE_TRUNC(timestamp, DAY) AS date,
    COUNT(*) AS blocks_created_ds
  FROM
    `bigquery-public-data.crypto_zilliqa.ds_blocks`
  GROUP BY
    date
),
tx_blocks_metrics AS (
  SELECT
    DATE_TRUNC(timestamp, DAY) AS date,
    COUNT(*) AS blocks_created_tx
  FROM
    `bigquery-public-data.crypto_zilliqa.tx_blocks`
  GROUP BY
    date
)

SELECT
  COALESCE(ds.date, tx.date) AS date,
  COALESCE(ds.blocks_created_ds, 0) AS blocks_created_ds,
  COALESCE(tx.blocks_created_tx, 0) AS blocks_created_tx
FROM
  ds_blocks_metrics ds
FULL OUTER JOIN
  tx_blocks_metrics tx
ON
  ds.date = tx.date
ORDER BY
  date
