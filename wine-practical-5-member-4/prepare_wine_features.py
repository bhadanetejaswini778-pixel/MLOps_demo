from pathlib import Path
import pandas as pd
from sklearn.datasets import load_wine
 
wine = load_wine(as_frame=True)
df = wine.frame.copy()
 
df["wine_class"] = df["target"].map(dict(enumerate(wine.target_names)))
df["sample_id"] = range(1, len(df) + 1)
df["event_timestamp"] = pd.Timestamp.now(tz="UTC").floor("s")
 
df["phenols_flavanoids_ratio"] = (
    df["total_phenols"] / df["flavanoids"].replace(0, 1)
)
df["color_proline_ratio"] = (
    df["color_intensity"] / df["proline"].replace(0, 1)
)
 
df = df.rename(columns={
    "od280/od315_of_diluted_wines": "od280_od315_diluted_wines"
})
 
Path("data").mkdir(exist_ok=True)
df.to_parquet("data/wine_features.parquet", index=False)
 
print("Wine feature data created")
print("Dataset shape:", df.shape)
print("Saved: data/wine_features.parquet")
