import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet("test.parquet")

event_counts = df['event_type'].value_counts()

event_counts.plot(kind='bar')

plt.title("Cart vs Purchase Events")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.tight_layout()

plt.show()