import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_parquet("test.parquet")

# Convert price to numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')

customer_data = df.groupby('user_id').agg({
    'product_id': 'count',
    'price': 'mean'
}).reset_index()

customer_data.columns = ['user_id', 'total_interactions', 'avg_price']

customer_data = customer_data.dropna()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(
    customer_data[['total_interactions', 'avg_price']]
)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
customer_data['cluster'] = kmeans.fit_predict(scaled_data)

print(customer_data.head())

print("\nCustomers in each cluster:")
print(customer_data['cluster'].value_counts())