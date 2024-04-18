以太坊（Ethereum）为外部使用提供了一系列的API，这些API允许开发者与以太坊区块链进行交互，包括读取数据和发送交易。以下是一些最常用的以太坊API：

### JSON-RPC API
以太坊客户端实现了JSON-RPC规范，提供了一套统一的方法供应用程序使用，无论具体的节点或客户端实现如何[9]。这些API包括但不限于：

- `eth_getBalance`：用于获取指定地址的以太币余额[1]。
- `eth_call`：执行合约方法的调用，不会在区块链上创建交易[8]。
- `eth_sendTransaction`：用于创建和发送交易，可以转移以太币或与智能合约交互。
- `eth_blockNumber`：获取最新区块的编号[6]。
- `eth_syncing`：检查节点的同步状态[6]。

### Web3.js
Web3.js是以太坊提供的一个JavaScript库，它封装了以太坊的RPC通信API，提供了一系列与区块链交互的方法[3][4]。常用的Web3.js API包括：

- `web3.eth`：用于与以太坊区块链和智能合约之间的交互[4]。
- `web3.utils`：包含一些辅助方法，如单位转换（`toWei`和`fromWei`）[4]。
- `web3.shh`：用于协议进行通信的P2P和广播[4]。

### Ethers.js
Ethers.js是另一个流行的JavaScript库，用于与以太坊区块链交互。它提供了一个简洁、一致的接口，例如：

- `Provider`：用于读取链上信息，不接触用户私钥，因此比Web3.js更安全[5]。

### Infura和Alchemy
Infura和Alchemy提供了即时、可扩展的API访问以太坊和IPFS网络。开发者可以注册并申请以太坊API KEY，利用它们的节点与区块链进行交互[7][13]。

### Geth
Geth是以太坊的一个客户端实现，它提供了一个交互式命令控制台，通过命令控制台可以访问以太坊的各种功能（API）[10]。

这些API是以太坊开发中最常用的，它们使得开发者能够构建各种去中心化应用（DApps），实现智能合约的部署和交云，以及与以太坊区块链的其他交互。

Citations:
[1] https://www.fmz.com/digest-topic/10010
[2] https://cloud.tencent.com/developer/article/1377234
[3] https://willzhuang.github.io/2018/03/14/%E4%BB%A5%E5%A4%AA%E5%9D%8A%E7%BC%96%E7%A8%8B-%E4%BD%BF%E7%94%A8web3%E5%92%8Cinfura/
[4] https://blog.csdn.net/m0_64494670/article/details/131566884
[5] https://www.wtf.academy/docs/ethers-101/Provider/
[6] https://www.cnblogs.com/veraland/p/15852117.html
[7] https://github.com/AmazingAng/WTF-Solidity/blob/main/Topics/Tools/TOOL04_Alchemy/readme.md
[8] https://support.huaweicloud.com/intl/zh-cn/devg-nes/zh-cn_topic_0000001669841684.html
[9] https://support.huaweicloud.com/intl/zh-cn/devg-nes/nes_devg_0013.html
[10] https://juejin.cn/s/blockchain.info%20testnet%20api
[11] https://blog.csdn.net/weixin_39842528/article/details/108283805
[12] https://support.huaweicloud.com/intl/zh-cn/devg-nes/zh-cn_topic_0000001669841688.html
[13] https://www.infura.io/zh/networks/ethereum/polygon
