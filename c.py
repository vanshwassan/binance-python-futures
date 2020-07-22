from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import json
import requests

request_client = RequestClient(api_key="iWNNGtIL103fyHuWi5G6WAyaH1rLj6fZt0iteNpwXDMYAqAyeaFn2OxOZHllb885", secret_key="Ub2W4UgRQ9QMh8MXfkeGAyU5O2mw2zGuCMVQbar9wGZJhJHp8SccAlAfg96ADm09")

acc = request_client.get_account_information()

print("Welcome Binance User!")
print("====== Your Balances ======")
print("Total Margin Balance: ", acc.totalMarginBalance)
print("Total Wallet Balance: ", acc.totalWalletBalance)
print("===========================")
bs = int(input("\nInput '1' to place LIMIT ORDER: "))
if (bs == 1):
        print("\n--------------------------------------")
        print("\nLIMIT BUY")
        print("\n--------------------------------------")
        coin = str(input("\nInput your COIN to BUY: "))
        qty = float(input("\nInput your QUANTITY to BUY: "))
        price = float(input("\nInput PRICE: "))
        lev = str(input("\nInput LEVERAGE: "))
        leverage = request_client.change_initial_leverage(symbol=coin, leverage=lev)
        conf = str(input("\nPLACE ORDER? ( Y / CTRL^C ): "))
        if (conf == "Y" or "y"):
            print("\nPlacing Order...")
            buy = request_client.post_order(symbol=coin, side=OrderSide.BUY, ordertype=OrderType.LIMIT, price=price, quantity=qty, timeInForce=TimeInForce.GTC)

else:
        print("FAILED TO PLACE ORDER!")
