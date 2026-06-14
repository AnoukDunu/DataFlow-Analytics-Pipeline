from database.connection import engine
import pandas as pd

def load_final(df):
    # use an engine-managed transaction so commits happen automatically
    try:
        with engine.begin() as conn:
            existing = pd.read_sql("SELECT id FROM cln_products", conn)

            df_to_load = df[~df['id'].isin(existing['id'])]

            if df_to_load.empty:
                print("No new unique records to load into final table.")
                return

            df_to_load.to_sql('cln_products', conn, if_exists='append', index=False)
            print("Data loaded into final table successfully.")
    except Exception as e:
        print(f"An error occurred while loading data into the final table: {e}")
    