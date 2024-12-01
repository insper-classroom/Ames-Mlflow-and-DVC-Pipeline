""" Defines the FeatureView for the housing dataset. """

from datetime import timedelta
from pathlib import Path

from feast import (
    Entity,
    FeatureView,
    Field,
    FileSource,
)
from feast.types import Int64, Float64

# Define the path to your housing dataset
DATA_PARQUET = str(Path.cwd() / "data" / "ames_processed.parquet")

# Define the primary entity using synthetic_id
house = Entity(name="house", join_keys=["synthetic_id"])

# Define the FileSource for the housing dataset
housing_stats_source = FileSource(
    name="housing_stats_source",
    path=DATA_PARQUET,
    timestamp_field="date",  # Matches the 'date' column
    created_timestamp_column="created",  # Optional, ensure it's in your dataset
)

# Define the FeatureView
housing_stats_fv = FeatureView(
    name="housing_stats",
    entities=[house],
    ttl=timedelta(days=1),
    schema=[
        Field(name="Fireplaces", dtype=Float64),
        Field(name="Kitchen.Qual", dtype=Int64),
        Field(name="Remod.Age", dtype=Float64),
        Field(name="Open.Porch.SF", dtype=Float64),
        Field(name="Garage.Age", dtype=Float64),
        Field(name="Lot.Area", dtype=Float64),
        Field(name="Full.Bath", dtype=Float64),
        Field(name="BsmtFin.SF.1", dtype=Float64),
        Field(name="Garage.Cars", dtype=Float64),
        Field(name="X1st.Flr.SF", dtype=Float64),
        Field(name="Exter.Qual", dtype=Int64),
        Field(name="Total.Bsmt.SF", dtype=Float64),
        Field(name="Garage.Area", dtype=Float64),
        Field(name="Gr.Liv.Area", dtype=Float64),
        Field(name="Overall.Qual", dtype=Int64),
    ],
    online=True,
    source=housing_stats_source,
    tags={"team": "housing_analytics"},
)
