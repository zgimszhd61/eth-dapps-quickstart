from web3 import Web3

# 连接到以太坊节点，这里使用的是Infura的主网节点
infura_url = 'https://mainnet.infura.io/v3/xxx'
web3 = Web3(Web3.HTTPProvider(infura_url))

# 确保连接成功
if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect to Ethereum network")

# 替换下面的地址为你想要查询的以太坊地址
address = "xxx"

# 查询余额
balance = web3.eth.get_balance(address)

# 将wei转换为ether
balance_in_eth = web3.from_wei(balance, 'ether')

print(f"The balance of address {address} is: {balance_in_eth} ETH")

import requests
import json

url = 'https://mainnet.infura.io/v3/285fc71094704eb9a4df74e9abd1eb3e'

payload = {
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 1
}

headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers).json()

print(response)