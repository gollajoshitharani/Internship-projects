import pandas as pd

df = pd.read_parquet("test.parquet")

# Products most frequently added to cart or purchased
recommended = (
    df[df['event_type'].isin(['cart', 'purchase'])]
    .groupby('product_id')
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("Top Recommended Products:")
print(recommended)