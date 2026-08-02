from fredapi import Fred

from config import config



class FredAPI:


    def __init__(self):

        self.client = Fred(

            api_key=config.FRED_API_KEY

        )


    def get_indicator(
        self,
        indicator
    ):


        series = {

            "CPI":
                "CPIAUCSL",

            "INTEREST_RATE":
                "FEDFUNDS",

            "UNEMPLOYMENT":
                "UNRATE",

            "GDP":
                "GDP"

        }


        if indicator not in series:

            return {

                "error":
                "Unknown indicator"

            }


        data = self.client.get_series(

            series[indicator]

        )


        latest = data.iloc[-1]


        return {

            "indicator":
            indicator,

            "value":
            float(latest)

        }



fred_api = FredAPI()