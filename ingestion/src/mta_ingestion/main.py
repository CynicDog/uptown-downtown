import time
import datetime
from pathlib import Path
import sys

from mta_ingestion.fetcher import fetch_feed
from mta_ingestion.parser import parse_feed
from mta_ingestion.writer import write_jsonl
from mta_ingestion.config import (
    MTA_FEED_URL,
    HEADERS,
    POLL_INTERVAL_SECONDS,
    RAW_BASE_PATH,
)

sys.stdout.reconfigure(line_buffering=True)

RAW_PATH = RAW_BASE_PATH

def main() -> None:
    while True:
        ingestion_ts = datetime.datetime.now(tz=datetime.timezone.utc)
        file_path = None

        try:
            feed = fetch_feed(MTA_FEED_URL, HEADERS)
            rows = parse_feed(feed, ingestion_ts)

            if rows:
                file_path = write_jsonl(rows, RAW_PATH, ingestion_ts)

            if file_path:
                print(
                    f"[INFO] Ingested {len(rows)} rows at {ingestion_ts.isoformat()} "
                    f"→ {file_path}"
                )
            else:
                print(
                    f"[INFO] Ingested 0 rows at {ingestion_ts.isoformat()}"
                )

        except Exception as exc:
            print(f"[ERROR] ingestion failed: {exc}")

        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
