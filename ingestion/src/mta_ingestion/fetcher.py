import requests

from mta_ingestion.proto.com.google.transit.realtime import (
    gtfs_realtime_pb2,
)

FeedMessage = gtfs_realtime_pb2.FeedMessage


def fetch_feed(url: str, headers: dict) -> FeedMessage:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    feed = FeedMessage()
    feed.ParseFromString(response.content)
    return feed
