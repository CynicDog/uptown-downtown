#!/usr/bin/env bash
set -e

SPARK_HOME=${SPARK_HOME:-/opt/spark}

echo "Starting Spark Thrift Server..."
exec $SPARK_HOME/sbin/start-thriftserver.sh \
  --master local[*] \
  --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension \
  --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog \
  --packages io.delta:delta-spark_2.12:3.2.0