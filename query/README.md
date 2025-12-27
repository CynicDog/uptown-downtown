# MTA Query Service

Query live MTA trip data stored in **Delta Lake** format by the ingestion service.  
This service exposes the data via **Spark SQL / Hive Thrift Server**, allowing BI tools like **Apache Superset** to connect and query it.

## Connecting Apache Superset (Hive)

This service exposes a **Hive Thrift Server** endpoint that Superset can use.

### Connection URI

```
hive://delta_query:10000/default
```
> `delta_query` is the Docker service name of the Spark/Hive container. 

* **Host**: `delta_query`
* **Port**: `10000`
* **Database**: `default`

## Query the data

```sql
SELECT *
FROM delta.`/delta/mta_bronze`;
```

## Example Superset Query

```sql
SELECT
  route_id,
  trip_id,
  timestamp
FROM delta.`/delta/mta_bronze`;
ORDER BY timestamp DESC
LIMIT 100;
```
