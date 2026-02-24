import os
import pandas as pd
from src.utils.logger import get_logger
from src.utils.settings import Config
from src.utils.time import utc_now

logger = get_logger(__name__)
metrics = get_logger("metrics")


def get_latest_raw_file():
    """
    Returns the most recent CSV file from the raw data directory.
    """
    files = [
        f for f in os.listdir(Config.DATA_RAW_DIR)
        if f.endswith(".csv")
    ]

    if not files:
        logger.error("No raw CSV files found in DATA_RAW_DIR.")
        raise FileNotFoundError("No raw CSV files found.")

    latest = max(
        files,
        key=lambda f: os.path.getmtime(os.path.join(Config.DATA_RAW_DIR, f))
    )

    logger.info(f"Latest raw file detected: {latest}")
    return os.path.join(Config.DATA_RAW_DIR, latest)


def transform_sites():
    """
    Loads the latest raw CSV, applies transformations,
    and writes the processed output to the processed directory.
    """
    start_time = utc_now()

    try:
        raw_file = get_latest_raw_file()
        df = pd.read_csv(raw_file)

        logger.info(f"Loaded raw file: {raw_file}")
        metrics.info(f"raw_rows={len(df)}")

        # ---------------------------------------------------------
        # Apply your transformations here
        # ---------------------------------------------------------
        df["ingested_at_utc"] = utc_now().isoformat()

        # Example transformation:
        # df = df.rename(columns={"old": "new"})
        # df["processed_flag"] = True

        # ---------------------------------------------------------

        ts = utc_now().strftime(Config.TIMESTAMP_FORMAT)
        output_file = os.path.join(
            Config.DATA_PROCESSED_DIR,
            f"traffic_sites_processed_{ts}.csv"
        )

        df.to_csv(output_file, index=False)

        logger.info(f"Processed file saved: {output_file}")
        metrics.info(f"processed_rows={len(df)}")

    except Exception as e:
        logger.error(f"Transform failed: {e}")
        raise

    finally:
        duration = (utc_now() - start_time).total_seconds()
        metrics.info(f"transform_duration_sec={duration}")


if __name__ == "__main__":
    transform_sites()
