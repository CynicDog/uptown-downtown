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

## Run as Container 

### Build the Docker image
```bash
docker build -t mta-ingestion:latest .
```

### Run the container
```bash
docker run --rm \
    -v "$(pwd)/data/delta":/app/data/delta \
    -e DELTA_BASE_PATH=/app/data/delta \
    --name mta-ingestion \
    mta-ingestion:latest
```