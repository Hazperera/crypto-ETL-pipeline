# Crypto-ETL-Data Pipeline 

## Key Metrics for Blockchain Data Analysis
Block Creation Rate
•	Description: Measures the number of blocks created over time.
•	Tables Used: ds_blocks, tx_blocks

Block Creation Rate

Transaction Volume

Average Transaction Fee

Transaction Success Rate

Events Emitted by Smart Contracts

Average Block Size

Block Time Consistency

Node Uptime, Network Efficiency

Transaction Latency

Network Decentralization

Node Geographical Distribution

Gini Coefficient of Block Production 


Block Creation Fact (fact_block_creation)
- Metrics: Blocks created, average block size

Transaction Fact (fact_transaction)
- Metrics: Transaction count, average transaction fee, transaction success rate

Event Logs Fact (fact_event_logs)
- Metrics: Event count

Block Dimension (dim_block):
- Attributes: Block ID, timestamp, producer, size

Transaction Dimension (dim_transaction)
- Attributes: Transaction hash, block number, timestamp, gas price, gas used

