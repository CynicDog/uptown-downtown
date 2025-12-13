import time
import datetime

from mta_ingestion.config import (
    MTA_FEED_URL,
    HEADERS,
    POLL_INTERVAL_SECONDS,
    DELTA_PATH,
)
from mta_ingestion.fetcher import fetch_feed
from mta_ingestion.parser import parse_feed
from mta_ingestion.spark import create_spark_session

import sys
sys.stdout.reconfigure(line_buffering=True)

def main():
    spark = create_spark_session()

    while True:
        ingestion_ts = datetime.datetime.utcnow()

        try:
            feed = fetch_feed(MTA_FEED_URL, HEADERS)
            rows = parse_feed(feed, ingestion_ts)

            if rows:
                df = spark.createDataFrame(rows)
                (
                    df.write
                    .format("delta")
                    .mode("append")
                    .save(str(DELTA_PATH))
                )

            print(
                f"Ingested {len(rows)} rows at {ingestion_ts.isoformat()}"
            )

        except Exception as e:
            print(f"[ERROR] ingestion failed: {e}")

        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
