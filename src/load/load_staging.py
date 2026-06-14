from database.connection import get_connection

def load_staging(df):
    conn = get_connection()

    df.to_sql('staging_table', con=conn, if_exists='replace', index=False)
    print("Data loaded into staging table successfully.")
