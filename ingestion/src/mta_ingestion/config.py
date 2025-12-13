import os
from pathlib import Path

SPARK_DRIVER_MEMORY = os.getenv("SPARK_DRIVER_MEMORY", "2g")

SPARK_EXECUTOR_MEMORY = os.getenv("SPARK_EXECUTOR_MEMORY", "4g")

MTA_FEED_URL = (
    "https://api-endpoint.mta.info/"
    "Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
)

HEADERS = {
    "Accept": "application/x-protobuf",
}

POLL_INTERVAL_SECONDS = 30

DELTA_BASE_PATH = Path(
    os.getenv("DELTA_BASE_PATH", Path.cwd() / "data" / "delta")
)

DELTA_PATH = DELTA_BASE_PATH / "mta_trip_updates_bronze"