import os
import requests
import pandas as pd
from src.utils.logger import get_logger
from src.utils.settings import Config
from src.utils.time import utc_now

logger = get_logger(__name__)
metrics = get_logger("metrics")


def fetch_api_data():
    """
    Fetches data from the configured API endpoint.
    """
    start_time = utc_now()

    try:
        response = requests.get(
            Config.API_URL,
            headers={"Authorization": f"Bearer {Config.API_KEY}"},
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        logger.info("API request successful")
        metrics.info(f"api_status=success")

        return data

    except Exception as e:
        logger.error(f"API request failed: {e}")
        metrics.info("api_status=failure")
        raise

    finally:
        duration = (utc_now() - start_time).total_seconds()
        metrics.info(f"api_latency_sec={duration}")


def save_raw_csv(data):
    """
    Saves API data to a timestamped CSV in the raw directory.
    """
    df = pd.DataFrame(data)

    ts = utc_now().strftime(Config.TIMESTAMP_FORMAT)
    output_file = os.path.join(
        Config.DATA_RAW_DIR,
        f"traffic_sites_{ts}.csv"
    )

    df.to_csv(output_file, index=False)

    logger.info(f"Raw data saved: {output_file}")
    metrics.info(f"raw_rows={len(df)}")


def ingest():
    """
    Main ingestion workflow:
    - Fetch API data
    - Save to raw CSV
    """
    logger.info("Starting API ingestion")

    data = fetch_api_data()
    save_raw_csv(data)

    logger.info("API ingestion completed successfully")


if __name__ == "__main__":
    ingest()
