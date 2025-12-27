import json
import datetime
from pathlib import Path


def _serialize_row(row: dict) -> dict:
    return {
        k: (v.isoformat() if isinstance(v, datetime.datetime) else v)
        for k, v in row.items()
    }


def write_jsonl(
    rows: list[dict],
    base_path: Path,
    ingestion_ts: datetime.datetime,
) -> Path:
    """
    Write rows as JSON Lines into a time-partitioned directory and
    return the file path written.
    """
    partition_path = ingestion_ts.strftime("date=%Y-%m-%d/hour=%H")
    output_dir = base_path / partition_path
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / f"ingest_{int(ingestion_ts.timestamp())}.jsonl"

    with open(file_path, "a", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(_serialize_row(row)) + "\n")

    return file_path
