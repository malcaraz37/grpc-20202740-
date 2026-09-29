# Sesion 13 - Servidor gRPC (unario)
# Antes de correrlo: bash compilar.sh
import grpc
from concurrent import futures

import saludo_pb2        # generado por protoc: los mensajes
import saludo_pb2_grpc   # generado por protoc: la clase base del servicio


class SaludadorServicio(saludo_pb2_grpc.SaludadorServicer):

    # El nombre debe coincidir EXACTAMENTE con el rpc del .proto
    def SaludarUno(self, request, context):
        mensaje = f"Hola, {request.nombre}! Esto viene del servidor gRPC."
        return saludo_pb2.SaludoResponse(mensaje=mensaje)


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
saludo_pb2_grpc.add_SaludadorServicer_to_server(SaludadorServicio(), servidor)
servidor.add_insecure_port("[::]:50051")
servidor.start()
print("Servidor gRPC escuchando en el puerto 50051...")
servidor.wait_for_termination()
