
def transform_data(df):
    df = df[['id', 'title', 'price', 'description', 'category', 'image', 'rating']]

    # Extracting the nested JSON in 'rating' column into separate columns
    df['rating_rate'] = df['rating'].apply(lambda x: x.get('rate') if isinstance(x, dict) else None)
    df['rating_count'] = df['rating'].apply(lambda x: x.get('count') if isinstance(x, dict) else None)

    # Drop the original 'rating' column as it's no longer needed
    df = df.drop(columns=['rating'])

    # quality checks!
    df = df.dropna()
    df = df[df['price'] > 0]  #Remove products with non-positive prices

    # removing duplicates if any
    df = df.drop_duplicates(subset=['id'])

    # estimating the revenue using the current price and number of reviews
    df['estimated_revenue'] = df['price'] * df['rating_count']

    print("Data transformation successful.")
    return df