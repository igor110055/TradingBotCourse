import tkinter as tk
import logging
import pprint
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex_futures import BitmexFuturesClient
from  interface.root_component import Root

logger = logging.getLogger()
logger.setLevel(logging.INFO)


stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)




if __name__ =='__main__':
    binance = BinanceFuturesClient('d5fd694f19a8c4feeec259e7d74e244d69f1bedf8af4a49c9387e2ea20a57433','b874a84f38efff2941fe2fcd86e83056a670d581e8187bd9641f263f5acfda26',True, True)

    bitmex = BitmexFuturesClient("YaTEaHBxKCB4t9XRCIlWd2Nq", "FB-_2AK9FwGhBiAZQd59GhfHI2GCsffpq_aCKkfrUjRTELeX", True)

    #print(bitmex.place_order(bitmex.contracts['XBTUSD'], "Limit", 100.9, "Buy", price=20000, tif="GoodTillCancel"))
    #print(bitmex.cancel_order('1511f520-5412-4176-a797-c73458862fbb'))


    root = Root(binance, bitmex)
    root.mainloop()
