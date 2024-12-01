from pprint import pprint
from feast import FeatureStore
from datetime import datetime, timedelta
import pandas as pd
from pathlib import Path

# Path to the dataset
DATA_PARQUET = Path.cwd() / "feature_repo" / "data" / "ames_processed.parquet"

# Initialize the FeatureStore
store = FeatureStore(repo_path="feature_repo")

# Load your housing dataset
housing_df = pd.read_parquet(DATA_PARQUET)

# Create a 'date' column by subtracting 'Remod.Age' from the current date
current_date = datetime.now()
housing_df["date"] = housing_df["Remod.Age"].apply(
    lambda x: current_date - timedelta(days=int(x * 365))
)

# Generate a synthetic unique identifier
housing_df["synthetic_id"] = housing_df.index

# Prepare the DataFrame for Feast
entity_df = housing_df[["synthetic_id", "date"]].copy()
entity_df.rename(columns={"date": "event_timestamp"}, inplace=True)

# Fetch historical features
feature_vector = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "housing_stats:Fireplaces",
        "housing_stats:Kitchen.Qual",
    ],
).to_df()

# Print the resulting feature vector
pprint(feature_vector)
