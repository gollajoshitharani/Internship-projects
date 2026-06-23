import pandas as pd

df = pd.read_parquet("test.parquet")

# Top 10 recommended products
recommendations = (
    df.groupby("product_id")
      .size()
      .sort_values(ascending=False)
      .head(10)
)

print("Top Recommended Products:")
print(recommendations)