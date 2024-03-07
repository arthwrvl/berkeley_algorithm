import grpc
import berkeley_pb2
import berkeley_pb2_grpc

def run():
    currentTime = 4
    client_id = '123'
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = berkeley_pb2_grpc.BerkeleyStub(channel)
        response = stub.Connect(berkeley_pb2.ConnectionRequest(client_id=client_id, time=currentTime))
        print("Server response:", response.message)
        while(True):
            print(f"Horário atual: {currentTime}")
            print("digite R para atualizar o relógio")
            inp = str(input())
            if inp == 'r':
                response = stub.SyncClocks(berkeley_pb2.TimeRequest(client_id=client_id, time=currentTime))
                print(response.message)
                currentTime += response.time
                print(currentTime)


if __name__ == '__main__':
    run()