from database.connection import get_connection
import pandas as pd

def load_final(df):
    conn = get_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        # make a safe copy so we do not modify the original DataFrame upstream
        df = df.copy()

        # remove duplicate rows in the incoming batch by id first
        # df = df.drop_duplicates(subset=['id'])

        # read existing ids from the final table
        existing_data = pd.read_sql("SELECT id FROM cln_products", conn)

        # cast ids to a consistent type before comparison
        # existing_ids = set(existing_data['id'].dropna().astype(str).tolist())
        # df['id'] = df['id'].astype(str)

        # keep only rows whose id is not already in the final table
        df = df[~df['id'].isin(existing_data['id'])]

        if df.empty:
            print("No new unique records to load into final table.")
            return

        df.to_sql('cln_products', conn, if_exists='append', index=False)
        print("Data incrementally loaded into final table successfully.")
    except Exception as e:
        print(f"An error occurred while loading data into the final table: {e}")
    finally:
        if conn is not None:
            conn.close()
