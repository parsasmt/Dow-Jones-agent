import yfinance as yf


class YahooFinanceAPI:


    def get_dow_jones(self):

        """
        Get current Dow Jones Industrial Average data.

        Yahoo ticker:
        ^DJI
        """

        ticker = yf.Ticker("^DJI")


        info = ticker.history(
            period="1d",
            interval="1m"
        )


        if info.empty:

            return {
                "error": "No market data available"
            }


        latest = info.iloc[-1]


        return {

            "symbol": "^DJI",

            "price": round(
                float(latest["Close"]),
                2
            ),

            "open": round(
                float(latest["Open"]),
                2
            ),

            "high": round(
                float(latest["High"]),
                2
            ),

            "low": round(
                float(latest["Low"]),
                2
            ),

            "volume": int(
                latest["Volume"]
            )

        }



yahoo_api = YahooFinanceAPI()