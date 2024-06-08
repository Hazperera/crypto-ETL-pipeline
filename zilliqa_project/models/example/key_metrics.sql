
-- Block Creation Rate

SELECT
  DATE_TRUNC(timestamp, DAY) AS day,
  COUNT(*) AS blocks_created
FROM
  `bigquery-public-data.crypto_zilliqa.ds_blocks`
GROUP BY
  day
ORDER BY
  day;