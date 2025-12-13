#!/usr/bin/env bash
set -e

echo "Cleaning Spark + Delta caches"

# Delta / Spark Ivy caches
rm -rf ~/.ivy2/cache/io.delta
rm -rf ~/.ivy2/jars/io.delta*
rm -rf ~/.ivy2/jars/spark*

# Local Delta data
rm -rf data/delta

# Python bytecode (safe to delete)
find src -type d -name "__pycache__" -exec rm -rf {} +
find src -type f -name "*.pyc" -delete

echo "Killing lingering Spark / JVM processes"
pkill -9 -f SparkSubmit || true
pkill -9 -f pyspark || true
pkill -9 -f java || true

sleep 2

echo "Recreating local delta directories"
mkdir -p data/delta/warehouse
mkdir -p data/delta/mta_trip_updates_bronze

export DELTA_BASE_PATH="$(pwd)/data/delta"

echo "Running ingestion app"
uv pip install -e .
uv run --with-editable . python -m mta_ingestion.main
