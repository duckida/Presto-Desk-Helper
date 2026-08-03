import network
import requests
import time
from presto import Presto
import json

presto = Presto()

presto.connect()   
# Make GET request
def get_time():
    try:
        response = requests.get("https://gateway.timeapi.world/timezone/Europe/London", headers={"x-rapidapi-key": "1fa031b1ddmsh6269abb2d931465p130deejsn5c1cda14dd16"})
        # Get response content
        response_content = json.loads(response.content)
        
        # Print results
        print('Response content:', response_content)
        print(f'time: {response_content["datetime"]}')
        
        return response_content["datetime"]

    except Exception as e:
        print('An error occurred during the request:', str(e))

if __name__ == "__main__":
    get_time()