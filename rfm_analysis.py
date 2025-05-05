import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import os

# Create output folders if not exist
os.makedirs("output", exist_ok=True)
os.makedirs("visuals", exist_ok=True)

# Load data
fact_df = pd.read_csv("data/Fact.csv")
customer_df = pd.read_csv("data/Customer.csv")
date_df = pd.read_csv("data/Date.csv")

# Clean column names
fact_df.columns = fact_df.columns.str.strip()
customer_df.columns = customer_df.columns.str.strip()
date_df.columns = date_df.columns.str.strip()

# Use Customer Key directly
df = fact_df.copy()
df['CustomerID'] = df['Customer Key']

# Convert YearPeriod to date (assume format is YYYY or YYYYMM)
if df['YearPeriod'].astype(str).str.len().max() <= 6:
    df['Date'] = pd.to_datetime(df['YearPeriod'].astype(str) + "01", format="%Y%m%d")
else:
    df['Date'] = pd.to_datetime(df['YearPeriod'])

# Ensure Revenue column exists and rename
df['Amount'] = df['Revenue']

# -------------------------------------
# Step 1: RFM Calculation
# -------------------------------------
snapshot_date = df['Date'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'Date': lambda x: (snapshot_date - x.max()).days,
    'CustomerID': 'count',
    'Amount': 'sum'
}).rename(columns={
    'Date': 'Recency',
    'CustomerID': 'Frequency',
    'Amount': 'Monetary'
}).reset_index()

# Save RFM
rfm.to_csv("output/rfm_raw.csv", index=False)

# -------------------------------------
# Step 2: Clustering with K-Means
# -------------------------------------
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

# Find optimal K (Elbow Method)
wcss = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(rfm_scaled)
    wcss.append(kmeans.inertia_)

# Plot elbow
plt.figure(figsize=(8, 4))
plt.plot(range(1, 10), wcss, marker='o')
plt.title("Elbow Method for Optimal Clusters")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.savefig("visuals/elbow_plot.png")
plt.close()

# Final clustering with optimal K (choose K=4 as example)
k = 4
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
rfm['Segment'] = kmeans.fit_predict(rfm_scaled)

# -------------------------------------
# Step 3: Churn Prediction Model (Mock)
# -------------------------------------
# Add mock churn labels for demonstration
import numpy as np
rfm['Churn'] = np.where(rfm['Recency'] > rfm['Recency'].median(), 1, 0)

X = rfm[['Recency', 'Frequency', 'Monetary']]
y = rfm['Churn']

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)
rfm['Churn_Predicted'] = clf.predict(X)

# Save final output
rfm.to_csv("output/rfm_churn_predictions.csv", index=False)

# Done
print("✅ RFM segmentation and churn prediction completed.")
print("📁 Outputs saved to: output/")
print("📊 Elbow plot saved to: visuals/elbow_plot.png")
