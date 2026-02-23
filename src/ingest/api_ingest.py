import pandas as pd
import os
from datetime import datetime
from utils.logger import get_logger

logger = get_logger("ingest")

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

def ingest_sites_csv():
    source_path = os.path.join(RAW_DIR, "traffic_sites.csv")

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source CSV not found at {source_path}")

    df = pd.read_csv(source_path)

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    dest_path = os.path.join(RAW_DIR, f"traffic_sites_{ts}.csv")

    df.to_csv(dest_path, index=False)
    logger.info(f"Ingested traffic sites CSV → {dest_path}")

    return dest_path

if __name__ == "__main__":
    try:
        ingest_sites_csv()
    except Exception as e:
        logger.exception(f"Ingestion failed: {e}")
