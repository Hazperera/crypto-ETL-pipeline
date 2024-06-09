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
  d.date,
  COALESCE(ds.blocks_created_ds, 0) AS blocks_created_ds,
  COALESCE(tx.blocks_created_tx, 0) AS blocks_created_tx
FROM
  {{ ref('dim_date') }} d
  LEFT JOIN ds_blocks_metrics ds ON d.date = ds.date
  LEFT JOIN tx_blocks_metrics tx ON d.date = tx.date
ORDER BY
  d.date