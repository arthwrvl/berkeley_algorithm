import grpc
import time
from concurrent.futures import ThreadPoolExecutor
import berkeley_pb2
import berkeley_pb2_grpc

class BerkeleyServicer(berkeley_pb2_grpc.BerkeleyServicer):
    def __init__(self, server_time):
        self.clients = {}
        self.server_time = server_time

    def GetTime(self, request, context):
        return berkeley_pb2.TimeResponse(time=self.server_time)



    def SyncClocks(self, request, context):
        cli_address = context.peer()
        cli_time = round(request.client_time, 2)
        self.clients[cli_address] = cli_time
        offset = avg_time(servicer)
        self.server_time = offset
        print(offset)
        print(f"horário atual do servidor {self.server_time}")
        cli_offset = self.server_time - cli_time
        return berkeley_pb2.ConnectionResponse(offset=cli_offset)

def avg_time(servicer):
    average = 0
    for client in servicer.clients:
        average += servicer.clients[client] 
    average += servicer.server_time
    average /= len(servicer.clients) + 1
    return average

def serve(servicer):
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    berkeley_pb2_grpc.add_BerkeleyServicer_to_server(servicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Esperando conexões")
    server.wait_for_termination()

if __name__ == '__main__':
    server_time = float(input("Digite a hora atual: "))
    servicer = BerkeleyServicer(server_time=server_time)
    serve(servicer)