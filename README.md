# Unidad II · gRPC — Programación Distribuida

Facultad de Telemática · Universidad de Colima

Este repositorio es tu laboratorio para toda la Unidad II (sesiones 11 a 16).
Trabajas en **tu propia copia**, nunca en el original.

## 1. Crea tu copia y tu Codespace (una sola vez)

1. Botón verde **Use this template → Create a new repository**.
   Nombre sugerido: `grpc-TU_MATRICULA`.
2. En tu copia: **Code → Codespaces → Create codespace on main**.
3. Espera a que termine de construirse (2–3 minutos la primera vez).
   Al final se instala solo `grpcio` y `grpcio-tools`.

## 2. Verifica tu entorno (Sesión 11)

En la terminal:

```bash
python verificar_entorno.py TU_MATRICULA
```

Toma una captura de lo que imprime: es tu evidencia de la Sesión 11.

## 3. Compila el contrato (Sesión 12)

```bash
bash compilar.sh
```

Genera `saludo_pb2.py` y `saludo_pb2_grpc.py`. Repítelo **cada vez** que cambies `saludo.proto`.

## 4. Corre servidor y cliente (Sesión 13)

Abre dos terminales (ícono **+** del panel de terminal):

```bash
# Terminal 1
python servidor.py

# Terminal 2 (con el servidor ya corriendo)
python cliente.py
```

## Errores reales, ya resueltos

| Mensaje | Por qué pasa | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'saludo_pb2'` | No has compilado el `.proto`. | `bash compilar.sh` |
| `ModuleNotFoundError: No module named 'grpc'` | No se instalaron las dependencias. | `pip install -r requirements.txt` |
| El servidor arranca dos veces sin error | En Linux, gRPC permite que dos servidores compartan el puerto 50051 (a diferencia de los sockets de la Unidad I, que marcaban `Address already in use`). Tus llamadas pueden caer en el servidor viejo. | Cierra con `Ctrl+C` la terminal del servidor anterior antes de volver a correrlo. |
| `StatusCode.UNAVAILABLE ... failed to connect to all addresses` | El cliente arrancó y no hay servidor escuchando. | Corre primero `python servidor.py` en otra terminal. |

## Cuida tu cuota de Codespaces

Cerrar la pestaña **no** detiene el Codespace. Al terminar: github.com/codespaces → `…` → **Stop codespace**.
