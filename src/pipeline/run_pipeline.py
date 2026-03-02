#This orchestrates:
#ingest, transform, load, metrics, logging

 from src.ingest.api_ingest import ingest_sites
from src.transform.transform_sites import transform_sites
from src.load.load_sites import load_sites

def run_pipeline():
    raw_df = ingest_sites()
    processed_df = transform_sites(raw_df)
    load_sites(processed_df)

if __name__ == "__main__":
    run_pipeline()
