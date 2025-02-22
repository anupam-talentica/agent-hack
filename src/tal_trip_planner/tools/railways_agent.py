from crewai.tools import BaseTool
import requests

class RailwaysAgent(BaseTool):
    name: str = "Custom API Tool"
    description: str = "Calls a specific REST API with parameters and headers"

    def _run(self, url: str, params: dict, headers: dict) -> str:
        try:
            url = "https://irctc1.p.rapidapi.com/api/v2/getFare",
            headers = {
                "x-rapidapi-host": "irctc1.p.rapidapi.com",
                "x-rapidapi-key": "api_key"
            },
            params= {
                "trainNo": "19038",
                "fromStationCode": "ST",
                "toStationCode": "BVI"
            }
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return f"Error calling API: {str(e)}"