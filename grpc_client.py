import grpc
from grpc_server import test_pb2
from grpc_server import test_pb2_grpc


with grpc.insecure_channel('localhost:50051') as channel:
    stub = test_pb2_grpc.TestControllerStub(channel)
    for test in stub.List(test_pb2.TestListRequest()):
        print(test, end='')