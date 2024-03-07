import grpc
import time
from concurrent.futures import ThreadPoolExecutor
import berkeley_pb2
import berkeley_pb2_grpc

class BerkeleyServicer(berkeley_pb2_grpc.BerkeleyServicer):
    def __init__(self):
        self.clients = {}
        self.currentTime = 0

    def Connect(self, request, context):
        client_id = request.client_id
        self.clients[client_id] = request.time
        return berkeley_pb2.ConnectionResponse(message=f"{client_id} Conectado!")


    def SyncClocks(self, request, context):
        averageTime = 0
        for client in self.clients:
            print("horário dos clientes: ",self.clients[client])
            averageTime += (self.clients[client] - self.currentTime)
        
        averageTime /= (len(self.clients) + 1)
        print("horário médio", averageTime)
        self.currentTime = self.currentTime + averageTime
        print("horário definitivo", self.currentTime)
        diffTime = self.currentTime - request.time
        message = f"o horário é: {self.currentTime}, altere {diffTime} no seu relógio"
        for client in self.clients:
            self.clients[client] = self.currentTime
        return berkeley_pb2.TimeResponse(message=message, time=diffTime)

def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    berkeley_pb2_grpc.add_BerkeleyServicer_to_server(BerkeleyServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Esperando conexões")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()