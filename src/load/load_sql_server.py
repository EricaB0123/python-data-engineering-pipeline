from src.utils.settings import Config
import pandas as pd
from src.utils.db import get_engine
from src.utils.logger import get_logger

logger = get_logger("load")

def load_sites(df: pd.DataFrame):
    engine = get_engine()

    df.to_sql(
        "TrafficSites",
        engine,
        if_exists="append",
        index=False
    )

    logger.info("Loaded sites into SQL Server.")
