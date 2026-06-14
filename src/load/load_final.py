from database.connection import get_connection

def load_final(df):
    conn = get_connection()
    try:
        df.to_sql('cln_products', conn, if_exists='append', index=False)
        print("Data loaded into final table successfully.")
    except Exception as e:
        print(f"An error occurred while loading data into the final table: {e}")
    finally:
        if conn is not None:
            conn.close()