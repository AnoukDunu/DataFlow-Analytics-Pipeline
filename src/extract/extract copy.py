import requests
import pandas as pd

def extract(api_url):
    url = api_url

    try:
        response = requests.get(url)

        # added the below line to auto-raise an error if the HTTP request returned an unsuccessful status code (4xx or 5xx)
        response.raise_for_status()

        data = response.json()

        # although code 200 indicates a successful connection, it doesn't guarantee that the response body contains valid JSON data.
        # So I need to verify the payload data before parsing. 
        if data.get('status') != 'success':
            print(f"API returned an error: {data.get('message', 'Unknown error')}")
            return None
        else:
            # afterwards, safely parse the JSON response and convert it to a DataFrame
            df = pd.DataFrame(data)
            return df

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while parsing API response: {e}")
        return None

    #  
    #     # handle different JSON payload shapes (dict vs list)
    #     if isinstance(data, dict):
    #         if data.get('status') != 'success':
    #             print(f"API returned an error: {data.get('message', 'Unknown error')}")
    #             return None
    #         # if the dict contains a results/list field, try to use it
    #         if 'data' in data and isinstance(data['data'], (list, dict)):
    #             df = pd.DataFrame(data['data'])
    #             return df
    #         # otherwise attempt to convert the dict itself to a DataFrame
    #         df = pd.DataFrame([data])
    #         return df

    #     if isinstance(data, list):
    #         df = pd.DataFrame(data)
    #         return df

    #     print('Unexpected JSON format from API')
    #     return None
    
    # except requests.exceptions.RequestException as e:
    #     print(f"An error occurred while making the API request: {e}")
    #     return None
    # except Exception as e:
    #     print(f"An unexpected error occurred while parsing API response: {e}")
    #     return None