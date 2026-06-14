# This is the main entry point for the application. It initializes the application and starts the main loop.
# The pipeline orchestration is also handled here, ensuring that all components are properly initialized and executed in the correct order.

# from config import Config
from extract.extract import extract
from database.connection import get_connection
from load.load_staging import load_staging

def run_pipeline():
    # Load configuration
    # config = Config()

    # Extract data from API
    api_url = "https://fakestoreapi.com/products"
    df = extract(api_url)
    

    # testing connection to database
    # connection = get_connection()

    if df is not None:
        print("Data extraction successful.")
        print(df.head())  # Display the first few rows of the extracted DataFrame
        # Load data into staging table ========TEMPORARY========
        load_staging(df)
        return df
    else:
        print("Data extraction failed.")
        return None
    

 

    

if __name__ == "__main__":
    run_pipeline()