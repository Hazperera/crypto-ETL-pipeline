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

DAILY_AVERAGE_GAS_USAGE_PER_TRANSACTION='''
SELECT 
    DATE(TIMESTAMP_TRUNC(block_timestamp, DAY)) AS date,
    AVG(gas_price * gas_limit) AS average_gas_per_transaction
FROM `public-data-finance.crypto_zilliqa.transactions`
GROUP BY date
ORDER BY date DESC
'''

TRANSACTION_SUCCES_RATE = '''
SELECT 
    DATE(block_timestamp) AS date,
    SUM(CASE WHEN success = TRUE THEN 1 ELSE 0 END) AS successful_transactions,
    COUNT(id) AS total_transactions,
    SUM(CASE WHEN success = TRUE THEN 1 ELSE 0 END) / COUNT(id) AS success_rate
FROM `public-data-finance.crypto_zilliqa.transactions`
GROUP BY date
ORDER BY date DESC
'''