from feast import FeatureStore
 
store = FeatureStore(repo_path=".")
 
features = store.get_online_features(
    features=[
        "wine_measurements:alcohol",
        "wine_measurements:malic_acid",
        "wine_measurements:flavanoids",
        "wine_measurements:proline",
    ],
    entity_rows=[
        {"sample_id": 1},
        {"sample_id": 2},
    ],
).to_dict()
 
print("Online feature retrieval completed")
print(features)
