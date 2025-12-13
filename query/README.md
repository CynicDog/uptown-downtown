# MTA Query Service

Query live MTA trip data stored in Delta format by the ingestion service.

## Access the query container

```bash
docker exec -it --user root mta_query bash
````

## Run Spark SQL with Delta support

```bash
/opt/spark/bin/spark-sql \
    --packages io.delta:delta-spark_2.12:3.2.0 \
    --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension \
    --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog \
    --conf spark.jars.ivy=/tmp/.ivy2
```

## Query the data

```sql
CREATE TABLE IF NOT EXISTS mta_trips
USING DELTA
LOCATION '/delta/mta_trip_updates_bronze';
SELECT * FROM mta_trips LIMIT 10;
```