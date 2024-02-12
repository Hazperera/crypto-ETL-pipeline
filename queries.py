# Define SQL queries as constants

MONTHLY_ACTIVE_ADDRESSES = '''
SELECT 
    DATE(TIMESTAMP_TRUNC(block_timestamp, MONTH, "UTC")) AS month,
    COUNT(DISTINCT sender) AS active_addresses
FROM `public-data-finance.crypto_zilliqa.transactions`
GROUP BY month
ORDER BY month DESC
'''

DAILY_TRANSACTION_VOLUME = '''
SELECT 
    DATE(TIMESTAMP_TRUNC(block_timestamp, DAY)) AS date,
    SUM(amount) AS total_volume
FROM `public-data-finance.crypto_zilliqa.transactions`
GROUP BY date
ORDER BY date DESC
'''
