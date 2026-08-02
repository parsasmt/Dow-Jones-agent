from tavily import TavilyClient

from config import config



class TavilyAPI:


    def __init__(self):

        self.client = TavilyClient(
            api_key=config.TAVILY_API_KEY
        )


    def search_financial_news(
        self,
        query: str,
        max_results: int = 5
    ):

        response = self.client.search(

            query=query,

            search_depth="advanced",

            max_results=max_results,

            topic="news"

        )


        results = []


        for item in response["results"]:

            results.append({

                "title": item.get(
                    "title"
                ),

                "content": item.get(
                    "content"
                ),

                "url": item.get(
                    "url"
                )

            })


        return results



tavily_api = TavilyAPI()