from database.connection import get_connection
import pandas as pd

def load_final(df):
    conn = get_connection()
    try:
        # checking for duplicate IDs to avoid inserting duplicate records into the final table. This is a simple check.
        existing_data = pd.read_sql("SELECT id FROM cln_products", conn)
        df = df[~df['id'].isin(existing_data['id'])]
   
        df.to_sql('cln_products', conn, if_exists='append', index=False)
        print("Data incrementally loaded into final table successfully.")
    except Exception as e:
        print(f"An error occurred while loading data into the final table: {e}")
    finally:
        if conn is not None:
            conn.close()