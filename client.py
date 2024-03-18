import grpc
import berkeley_pb2
import berkeley_pb2_grpc
import time

def run():
    

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = berkeley_pb2_grpc.BerkeleyStub(channel)
        response = stub.GetTime(berkeley_pb2.TimeRequest())
        print("horário do servidor:", response.time)
        current_time = float(input("Digite a hora atual: "))
        while(True):
            time.sleep(3)    
            response = stub.SyncClocks(berkeley_pb2.ConnectionRequest(client_time=current_time))
            current_time += response.offset
            print(f"sua hora deve ser: {current_time}")


if __name__ == '__main__':
    run()