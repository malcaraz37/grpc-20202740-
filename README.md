# Unidad II: gRPC y Protocol Buffers - Programacion Distribuida

Facultad de Telematica · Universidad de Colima  
Estudiante: Manuel Alcaraz  
Matricula: 20202740  

---

## Descripcion General

Este repositorio constituye el laboratorio de practicas para la Unidad II de la materia Programacion Distribuida (sesiones 11 a 16). El objetivo principal es comprender la arquitectura de llamadas a procedimientos remotos (gRPC), el uso de Protocol Buffers (Proto3) como Lenguaje de Definicion de Interfaces (IDL) y el formato de serializacion binaria eficiente para la transmision de datos en la red.

---

## Estructura del Proyecto

* **saludo.proto**: Archivo de contrato donde se definen los servicios, metodos RPC y las estructuras de mensajes (IDL).
* **compilar.sh**: Script de compilacion automatica que invoca el compilador `protoc` para generar los stubs de cliente y servidor en Python.
* **ver_bytes.py**: Script de diagnostico para inspeccionar la serializacion binaria de Protocol Buffers, etiquetas de casillas, bytes resultantes y comparativa de tamano frente a JSON.
* **verificar_entorno.py**: Script para validar que las librerias `grpcio` y `grpcio-tools` esten correctamente instaladas en el entorno.
* **servidor.py**: Implementacion del servidor gRPC que expone el servicio `Saludador`.
* **cliente.py**: Implementacion del cliente gRPC que consume el servicio `Saludador`.
* **requirements.txt**: Lista de dependencias de Python requeridas para el proyecto.

---

## Instalacion y Requisitos

Para ejecutar los programas de este repositorio se requiere Python 3.10 o superior y las herramientas de desarrollo gRPC.

### Instalacion de dependencias

```bash
pip install -r requirements.txt
```

Dependencias principales:
* `grpcio`: Motor y entorno de ejecucion de gRPC para Python.
* `grpcio-tools`: Compilador de Protocol Buffers (`protoc`) integrado para Python.

---

## Guia de Uso por Sesiones

### 1. Verificacion del Entorno (Sesion 11)

Valida que el interprete de Python y los paquetes de gRPC esten listos:

```bash
python verificar_entorno.py 20202740
```

### 2. Definicion y Compilacion del Contrato (Sesion 12)

El contrato [saludo.proto](saludo.proto) define el servicio `Saludador` y los mensajes `SaludoRequest` y `SaludoResponse`:

```protobuf
syntax = "proto3";

package saludo;

service Saludador {
  rpc SaludarUno (SaludoRequest) returns (SaludoResponse);
}

message SaludoRequest {
  string nombre = 1;
  string matricula = 2;
}

message SaludoResponse {
  string mensaje = 1;
}
```

#### Compilacion del contrato

Cada vez que se modifique el archivo `.proto`, se debe recompilar para regenerar `saludo_pb2.py` (mensajes) y `saludo_pb2_grpc.py` (servicer y stub).

* **En entornos Linux / Bash / Codespaces:**
  ```bash
  bash compilar.sh
  ```
* **En entornos Windows (PowerShell / CMD):**
  ```powershell
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. saludo.proto
  ```

### 3. Inspeccion de la Serializacion en Bytes (Sesion 12 - Bloque 05)

Para verificar como viajan los datos en formato binario por la red:

```bash
python ver_bytes.py "Manuel Alcaraz" 20202740
```

#### Fundamento del Formato Binario (Wire Format)

Protocol Buffers no envia los nombres de los campos en texto (a diferencia de formatos como JSON o XML). En su lugar, utiliza un identificador binario denominado etiqueta (*Tag*):

$$\text{Etiqueta} = (\text{Numero de Casilla} \times 8) + \text{Wire Type}$$

Para campos de tipo texto (`string`), el *Wire Type* es `2` (Length-delimited):
* Casilla 1 (`nombre`): `(1 * 8) + 2 = 10` -> `0x0A` en hexadecimal.
* Casilla 2 (`matricula`): `(2 * 8) + 2 = 18` -> `0x12` en hexadecimal.
* Casilla 5 (`matricula`): `(5 * 8) + 2 = 42` -> `0x2A` en hexadecimal.

### 4. Ejecucion de Cliente y Servidor (Sesion 13)

Para ejecutar la comunicacion RPC completa, se requieren dos terminales:

1. **Terminal 1 (Iniciar Servidor):**
   ```bash
   python servidor.py
   ```

2. **Terminal 2 (Ejecutar Cliente):**
   ```bash
   python cliente.py
   ```

---

## Solucion de Problemas Comunes

| Error / Sintoma | Causa | Solucion |
|---|---|---|
| `ModuleNotFoundError: No module named 'saludo_pb2'` | No se ha compilado el contrato `.proto`. | Ejecutar `bash compilar.sh` o el comando `protoc`. |
| `ModuleNotFoundError: No module named 'grpc'` | Las librerias necesarias no estan instaladas. | Ejecutar `pip install -r requirements.txt`. |
| `StatusCode.UNAVAILABLE ... failed to connect` | El cliente inicio pero el servidor no esta activo. | Iniciar primero `python servidor.py` en otra terminal. |
| Datos incorrectos al cambiar numeros de casilla | Se modificaron los numeros de casilla de un servicio en produccion. | Nunca alterar el numero de casilla asignado a un campo ya existente para preservar compatibilidad hacia atras. |

---

## Notas de Buenas Practicas

* **Inmutabilidad de Casillas:** Nunca cambie el numero asignado a un campo una vez que el contrato este en uso, ya que rompe la compatibilidad binaria entre versiones de cliente y servidor.
* **Adicion de Campos:** Para extender un mensaje, agregue nuevos campos con numeros de casilla subsecuentes no utilizados.
