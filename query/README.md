# MTA Query Service

Query live MTA trip data stored in **Delta Lake** format by the ingestion service.  
This service exposes the data via **Spark SQL / Hive Thrift Server**, allowing BI tools like **Apache Superset** to connect and query it.

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
SELECT *
FROM delta.`/delta/mta_trip_updates_bronze`;
```

## Connecting Apache Superset (Hive)

This service exposes a **Hive Thrift Server** endpoint that Superset can use.

### Connection URI

```
hive://mta_query:10000/default
```

* **Host**: `query`
* **Port**: `10000`
* **Database**: `default`

> `query` is the Docker service name of the Spark/Hive container.

## Example Superset Query

```sql
SELECT
  route_id,
  trip_id,
  timestamp
FROM delta.`/delta/mta_trip_updates_bronze`;
ORDER BY timestamp DESC
LIMIT 100;
```
