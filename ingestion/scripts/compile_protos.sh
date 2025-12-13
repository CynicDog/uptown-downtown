#!/usr/bin/env bash
set -e

PROTO_ROOT=protos
OUT_ROOT=src/mta_ingestion/proto

mkdir -p ${OUT_ROOT}

python3 -m grpc_tools.protoc \
  --proto_path=${PROTO_ROOT} \
  --python_out=${OUT_ROOT} \
  ${PROTO_ROOT}/com/google/transit/realtime/gtfs-realtime.proto

python3 -m grpc_tools.protoc \
  --proto_path=${PROTO_ROOT} \
  --python_out=${OUT_ROOT} \
  ${PROTO_ROOT}/gtfs-realtime-NYCT.proto
