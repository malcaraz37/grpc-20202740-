#!/usr/bin/env bash
# Genera el codigo Python a partir de saludo.proto.
# Crea dos archivos: saludo_pb2.py (mensajes) y saludo_pb2_grpc.py (stub y servicer).
# Vuelve a correrlo CADA VEZ que cambies el .proto.
set -e
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. saludo.proto
echo "Listo: se generaron saludo_pb2.py y saludo_pb2_grpc.py"
