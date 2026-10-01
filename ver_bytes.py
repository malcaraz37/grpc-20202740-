# Sesion 12 - Asi viaja tu comanda: el mensaje convertido en bytes
# Uso: python ver_bytes.py "Tu nombre" TU_MATRICULA
# Antes: bash compilar.sh  (cada vez que cambies saludo.proto)
import sys
import json

try:
    import saludo_pb2
except ModuleNotFoundError:
    print("Todavia no existe saludo_pb2.py. Primero compila: bash compilar.sh")
    sys.exit(1)

if len(sys.argv) < 3:
    print('Uso: python ver_bytes.py "Tu nombre" TU_MATRICULA')
    sys.exit(1)

nombre, matricula = sys.argv[1], sys.argv[2]
campos = {f.name: f for f in saludo_pb2.SaludoRequest.DESCRIPTOR.fields}

peticion = saludo_pb2.SaludoRequest(nombre=nombre)
if "matricula" in campos:
    peticion.matricula = matricula
else:
    print("Aviso: SaludoRequest todavia no tiene el campo 'matricula'.")
    print("       Agregalo en saludo.proto, vuelve a compilar y repite.\n")

datos = peticion.SerializeToString()          # marshalling
como_json = json.dumps({k: getattr(peticion, k) for k in campos}, ensure_ascii=False).encode("utf-8")

print("=" * 60)
print(" TU COMANDA EN PROTOCOL BUFFERS  -  matricula", matricula)
print("=" * 60)
print(" Campos del contrato (SaludoRequest):")
for f in campos.values():
    etiqueta = (f.number << 3) | 2          # 2 = tipo 'texto' en el formato binario
    print(f"   casilla {f.number:>2} = {f.name:<10} -> viaja como la etiqueta 0x{etiqueta:02X}")
print("-" * 60)
print(" Bytes que viajan por la red:")
print("  ", datos.hex(" ").upper())
print(f" Tamano: {len(datos)} bytes   |   El mismo dato en JSON: {len(como_json)} bytes")
print("-" * 60)
recibido = saludo_pb2.SaludoRequest()
recibido.ParseFromString(datos)                # unmarshalling
print(" Del otro lado se reconstruye como:")
for linea in str(recibido).strip().splitlines():
    print("  ", linea)
print("=" * 60)
