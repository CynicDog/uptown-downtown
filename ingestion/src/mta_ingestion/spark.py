# spark.py
from pyspark.sql import SparkSession
from mta_ingestion.config import DELTA_BASE_PATH


def create_spark_session(app_name: str = "mta-ingestion") -> SparkSession:
    warehouse_dir = DELTA_BASE_PATH / "warehouse"

    return (
        SparkSession.builder
        .appName(app_name)
        .config(
            "spark.jars.packages",
            "io.delta:delta-spark_2.12:3.2.0",
        )
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension",
        )
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .config(
            "spark.sql.warehouse.dir",
            str(warehouse_dir),
        )
        .getOrCreate()
    )
