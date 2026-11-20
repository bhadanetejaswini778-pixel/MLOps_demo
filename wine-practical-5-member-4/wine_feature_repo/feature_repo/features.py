
from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64

wine_entity = Entity(
    name="wine_sample",
    join_keys=["sample_id"],
    description="Unique Wine dataset sample"
)

wine_source = FileSource(
    name="wine_source",
    path="data/wine_features.parquet",
    timestamp_field="event_timestamp"
)

wine_features = FeatureView(
    name="wine_measurements",
    entities=[wine_entity],
    ttl=timedelta(days=365),
    schema=[
        Field(name="alcohol", dtype=Float64),
        Field(name="malic_acid", dtype=Float64),
        Field(name="ash", dtype=Float64),
        Field(name="total_phenols", dtype=Float64),
        Field(name="flavanoids", dtype=Float64),
        Field(name="color_intensity", dtype=Float64),
        Field(name="proline", dtype=Float64),
        Field(name="phenols_flavanoids_ratio", dtype=Float64),
        Field(name="color_proline_ratio", dtype=Float64),
    ],
    source=wine_source
)
