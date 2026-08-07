import pandas as pd

# Load saved files
df_clustered_95 = pd.read_csv("skills_clustered_095.csv")
df_unique_95 = pd.read_csv("skills_unique_095.csv")
df_deduped_095_full = pd.read_csv("skills_deduplicated_095_full.csv")

print(f"Clustered (size>1): {len(df_clustered_95)}")
print(f"Unique (size=1): {len(df_unique_95)}")
print(f"Deduplicated full: {len(df_deduped_095_full)}")


# Find largest cluster
largest_center = df_clustered_95.groupby('cluster_center_id')['id'].count().idxmax()
largest_size = df_clustered_95.groupby('cluster_center_id')['id'].count().max()
largest_ids = df_clustered_95[
    df_clustered_95['cluster_center_id'] == largest_center
]['id'].tolist()

print(f"Largest cluster: {largest_size} skills")

# Get content from full file
largest_content = df_deduped_095_full[
    df_deduped_095_full['id'].isin(largest_ids)
]

for _, row in largest_content.head(5).iterrows():
    print(f"\n--- {row['name']} by {row['author']} (stars: {row['stars']}) ---")
    print(row['content_clean'][:300])
    print("-" * 60)
