# Ingestion Service

Polls MTA GTFS-Realtime feeds, parses protobuf messages, and writes near-real-time subway data to Delta Lake using Spark.

## Run locally

### Set up environment

```bash
uv sync
```

### Run ingestion

```bash
 ./scripts/run_locally.sh 
 ```

After the service starts successfully, you should see Delta Lake data created under the `data/` directory at the root of the ingestion service:
```
data/
└── delta/
    ├── warehouse/
    └── mta_trip_updates_bronze/
        ├── _delta_log/
        └── part-*.parquet
```