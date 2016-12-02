import time
from unittest import TestCase
from brokers.ib.tws import *
from swigibpy import Contract


class TestTWS(TestCase):
    class HistoricalDataHandler(object):
        def historicalData(self, request: Request, date, open_, high, low, close, volume, bar_count, wap, has_gaps):
            print("Req[%d] Historical=> %s - Open: %s, High: %s, Low: %s, Close: %s, Volume: %d" %
                  (request.request_id, date, open_, high, low, close, volume))

    class MarketDataHandler(object):
        def tickPrice(self, request: Request, field: int, price: float, can_auto_execute: int):
            print("Req[%d] Price=> Field: %d, Price: %s, Auto Execute: %s" %
                  (request.request_id, field, price, can_auto_execute))

        def tickSize(self, request: Request, field: int, size: int):
            print("Req[%d] Size=> Field: %d, Size: %d" % (request.request_id, field, size))

        def tickGeneric(self, request: Request, tick_type: int, value: float):
            print("Req[%d] Generic=> Tick Type: %d, Value: %s" % (request.request_id, tick_type, value))

        def tickString(self, request: Request, tick_type: int, value: str):
            print("Req[%d] String=> Tick Type: %d, Value: %s" % (request.request_id, tick_type, value))

    def test_reqHistoricalDataMultiple(self):
        handler = TestTWS.HistoricalDataHandler()
        tws = TwsClient(1)

        hhi = Contract()
        hhi.exchange = "HKFE"
        hhi.secType = "IND"
        hhi.symbol = "HHI.HK"
        hhi.currency = "HKD"

        hsi = Contract()
        hsi.exchange = "HKFE"
        hsi.secType = "IND"
        hsi.symbol = "HSI"
        hsi.currency = "HKD"

        with tws.connect():
            hsi_req = tws.reqHistoricalData(handler, hsi, "20160525 00:00:00", "1 D", BarSize.Sec30)
            hhi_req = tws.reqHistoricalData(handler, hhi, "20160525 00:00:00", "1 D", BarSize.Sec30)
            hsi_req.done.wait(30)
            hhi_req.done.wait(30)

    def test_reqMarketData(self):
        handler = TestTWS.MarketDataHandler()
        tws = TwsClient(2)

        aapl = Contract()
        aapl.exchange = "SMART"
        aapl.secType = "STK"
        aapl.symbol = "AAPL"
        aapl.currency = "USD"

        with tws.connect():
            aapl_req = tws.reqMarketData(handler, aapl, "233,236,258")
            time.sleep(2)
            aapl_req.cancel()
            time.sleep(1)

logging.basicConfig(level=logging.DEBUG)
