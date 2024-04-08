from web3 import Web3

# 连接到以太坊节点，这里使用的是Infura的主网节点
infura_url = 'https://mainnet.infura.io/v3/'
web3 = Web3(Web3.HTTPProvider(infura_url))

# 确保连接成功
if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect to Ethereum network")

# 替换下面的地址为你想要查询的以太坊地址
address = "0xDc698F8f9D8D8b5350BE1A5CdE21CA7eCe400E2D"

# 查询余额
balance = web3.eth.get_balance(address)

# 将wei转换为ether
balance_in_eth = web3.from_wei(balance, 'ether')

print(f"The balance of address {address} is: {balance_in_eth} ETH")

######

# 查询最新区块的编号
latest_block_number = web3.eth.block_number
print(f"Latest block number: {latest_block_number}")

# 查询最新区块的详细信息
latest_block = web3.eth.get_block(latest_block_number)
for tx_hash in latest_block['transactions']:
    print(tx_hash.hex())
    # 查询特定交易的详细信息
    transaction_details = web3.eth.get_transaction(tx_hash.hex())
    # print(f"Transaction details: {transaction_details}")
    print("======")
    print("from:" + transaction_details['from'])
    print("to:" + transaction_details['to'])
    print("gas:" + str(transaction_details['gas']))
    print("gasPrice:" + str(transaction_details['gasPrice']))
    # break
