from web3 import Web3
import secrets
connect = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
#kiểm tra xem đã kết thành công hay chưa
print(connect.isConnected())
#tạo private key
private_key = secrets.token_hex(32)
print("Private Key: "+ private_key)
#tạo vi tu private key
wallet = connect.eth.account.privateKeyToAccount(private_key)
print("Address :  " + wallet.address)