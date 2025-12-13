import datetime

from mta_ingestion.proto import gtfs_realtime_NYCT_pb2 as nyct_pb2


def parse_feed(feed, ingestion_ts: datetime.datetime) -> list[dict]:
    rows = []

    for entity in feed.entity:
        if not entity.HasField("trip_update"):
            continue

        trip_update = entity.trip_update
        trip = trip_update.trip

        nyct_trip = trip.Extensions[nyct_pb2.nyct_trip_descriptor]

        for stu in trip_update.stop_time_update:
            nyct_stop = stu.Extensions[
                nyct_pb2.nyct_stop_time_update
            ]

            arrival_time = None
            if (
                stu.HasField("arrival")
                and stu.arrival.HasField("time")
            ):
                arrival_time = datetime.datetime.fromtimestamp(
                    stu.arrival.time
                )

            rows.append(
                {
                    "ingestion_ts": ingestion_ts,
                    "trip_id": trip.trip_id,
                    "route_id": trip.route_id,
                    "direction": (
                        nyct_pb2.NyctTripDescriptor.Direction.Name(
                            nyct_trip.direction
                        )
                        if nyct_trip.HasField("direction")
                        else None
                    ),
                    "stop_id": stu.stop_id,
                    "arrival_time": arrival_time,
                    "scheduled_track": (
                        nyct_stop.scheduled_track or None
                    ),
                    "actual_track": (
                        nyct_stop.actual_track or None
                    ),
                    "is_assigned": nyct_trip.is_assigned,
                }
            )

    return rows
