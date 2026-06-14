import requests
import pandas as pd

def extract(api_url):
    url = api_url

    try:
        response = requests.get(url)

        # added the below line to auto-raise an error if the HTTP request returned an unsuccessful status code (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        df = pd.DataFrame(data)

        # The below line is added to simulate real-world issues like duplicate data or messy data. To add depth to the data and projhect.
        # please hire me :(
        df = pd.concat([df, df.iloc[:3]])
        
        print("Data extraction successful!")
        return df

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while parsing API response: {e}")
        return None