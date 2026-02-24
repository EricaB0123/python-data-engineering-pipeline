import pandas as pd
import os
#from datetime import datetime, UTC
from src.utils.settings import Config
from src.utils.time import utc_now


from src.utils.logger import get_logger

logger = get_logger("ingest")

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

def ingest_sites_csv():
    source_path = os.path.join(RAW_DIR, "traffic_sites.csv")

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source CSV not found at {source_path}")

    df = pd.read_csv(source_path)

    ts = utc_now().strftime(Config.TIMESTAMP_FORMAT)
    dest_path = os.path.join(Config.DATA_RAW_DIR, f"traffic_sites_{ts}.csv")


    df.to_csv(dest_path, index=False)
    logger.info(f"Ingested traffic sites CSV → {dest_path}")

    return dest_path

if __name__ == "__main__":
    try:
        ingest_sites_csv()
    except Exception as e:
        logger.exception(f"Ingestion failed: {e}")
