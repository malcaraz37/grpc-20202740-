# Sesion 11 - Verificacion del entorno
# Uso: python verificar_entorno.py TU_MATRICULA
import os
import sys
import platform
from datetime import datetime

if len(sys.argv) < 2:
    print("Falta tu matricula. Uso: python verificar_entorno.py TU_MATRICULA")
    sys.exit(1)

matricula = sys.argv[1]

try:
    import grpc
    import grpc_tools  # noqa: F401
except ModuleNotFoundError as e:
    print(f"Entorno incompleto: {e}")
    print("Solucion: pip install -r requirements.txt")
    sys.exit(1)

codespace = os.environ.get("CODESPACE_NAME", "(no es un Codespace: entorno local)")

print("=" * 52)
print(" ENTORNO LISTO PARA LA UNIDAD II - gRPC")
print("=" * 52)
print(f" Matricula : {matricula}")
print(f" Python    : {platform.python_version()}")
print(f" grpcio    : {grpc.__version__}")
print(f" Codespace : {codespace}")
print(f" Fecha     : {datetime.now():%Y-%m-%d %H:%M}")
print("=" * 52)
