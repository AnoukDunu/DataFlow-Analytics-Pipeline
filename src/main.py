# This is the main entry point for the application. It initializes the application and starts the main loop.
# The pipeline orchestration is also handled here, ensuring that all components are properly initialized and executed in the correct order.

# from config import Config
from extract.extract import extract
from database.connection import get_connection
from load.load_staging import load_staging
from transform.transform import transform_data
from load.load_final import load_final

def run_pipeline():
    # Load configuration
    # config = Config()

    # Extract data from API
    api_url = "https://fakestoreapi.com/products"
    df = extract(api_url)
    

    # testing connection to database
    # connection = get_connection()

    if df is not None:

        # Load data into staging table ========TEMPORARY========
        load_staging(df)
        # transforming data
        cleaned_df = transform_data(df)
        # load cleaned and transformed data into the final table
        load_final(cleaned_df)
        return cleaned_df
    else:
        print("Data extraction failed.")
        return None



if __name__ == "__main__":
    run_pipeline()