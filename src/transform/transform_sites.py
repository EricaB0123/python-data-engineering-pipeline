import os
import pandas as pd
from datetime import datetime
from src.utils.logger import get_logger


logger = get_logger("transform")

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

def load_latest_raw():
    """Load the most recent timestamped raw CSV."""
    files = sorted(
        [f for f in os.listdir(RAW_DIR) if f.startswith("traffic_sites_") and f.endswith(".csv")],
        reverse=True
    )

    if not files:
        raise FileNotFoundError("No timestamped raw traffic_sites CSV found.")

    latest = files[0]
    path = os.path.join(RAW_DIR, latest)
    logger.info(f"Loading raw file: {path}")

    return pd.read_csv(path)

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise column names to snake_case."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

def transform_sites(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardise the traffic sites dataset."""
    df = clean_column_names(df)

    # Select only the useful columns (adjust based on your CSV)
    expected_cols = [
        "site_id",
        "site_name",
        "region",
        "road_name",
        "start_km",
        "end_km",
        "latitude",
        "longitude",
        "carriageway",
        "direction",
        "status"
    ]

    df = df[[col for col in expected_cols if col in df.columns]]

    # Convert numeric fields
    numeric_cols = ["start_km", "end_km", "latitude", "longitude"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Add metadata
    df["ingested_at_utc"] = datetime.utcnow().isoformat()

    logger.info("Transformation complete.")
    return df

def save_processed(df: pd.DataFrame):
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(PROCESSED_DIR, f"traffic_sites_processed_{ts}.csv")
    df.to_csv(path, index=False)
    logger.info(f"Saved processed file: {path}")
    return path

if __name__ == "__main__":
    try:
        raw_df = load_latest_raw()
        processed_df = transform_sites(raw_df)
        save_processed(processed_df)
    except Exception as e:
        logger.exception(f"Transform step failed: {e}")
