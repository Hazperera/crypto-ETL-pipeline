-- models/dim_transaction_participants.sql

-- Transaction Participants

SELECT
  id,
  sender_pub_key,
  sender,
  signature,
  to_addr
FROM
  `bigquery-public-data.crypto_zilliqa.transactions`

