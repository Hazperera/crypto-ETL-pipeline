
-- models/fact_block_creation.sql

WITH ds_block_metrics AS (
  SELECT
    DATE_TRUNC(timestamp, DAY) AS day,
    COUNT(*) AS ds_blocks_created
  FROM
    `bigquery-public-data.crypto_zilliqa.ds_blocks`
  GROUP BY
    day
),
tx_block_metrics AS (
  SELECT
    DATE_TRUNC(timestamp, DAY) AS day,
    COUNT(*) AS tx_blocks_created
  FROM
    `bigquery-public-data.crypto_zilliqa.tx_blocks`
  GROUP BY
    day
)
SELECT
  d.day,
  COALESCE(ds.ds_blocks_created, 0) AS ds_blocks_created,
  COALESCE(tx.tx_blocks_created, 0) AS tx_blocks_created
FROM
  (SELECT DISTINCT DATE_TRUNC(timestamp, DAY) AS day FROM `bigquery-public-data.crypto_zilliqa.ds_blocks`
   UNION DISTINCT
   SELECT DISTINCT DATE_TRUNC(timestamp, DAY) AS day FROM `bigquery-public-data.crypto_zilliqa.tx_blocks`) d
LEFT JOIN ds_block_metrics ds ON d.day = ds.day
LEFT JOIN tx_block_metrics tx ON d.day = tx.day
ORDER BY
  d.day
