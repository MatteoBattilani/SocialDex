from web3 import Web3

w3 = Web3(Web3.HTTPProvider(
    'https://ropsten.infura.io/v3/d39bfbee2a9a4394a605955a1420583b'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f"Your address: {address}\nYour key: {privateKey}")
