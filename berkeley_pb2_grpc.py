# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import berkeley_pb2 as berkeley__pb2


class BerkeleyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTime = channel.unary_unary(
                '/Berkeley/GetTime',
                request_serializer=berkeley__pb2.TimeRequest.SerializeToString,
                response_deserializer=berkeley__pb2.TimeResponse.FromString,
                )
        self.SyncClocks = channel.unary_unary(
                '/Berkeley/SyncClocks',
                request_serializer=berkeley__pb2.ConnectionRequest.SerializeToString,
                response_deserializer=berkeley__pb2.ConnectionResponse.FromString,
                )


class BerkeleyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyncClocks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BerkeleyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTime,
                    request_deserializer=berkeley__pb2.TimeRequest.FromString,
                    response_serializer=berkeley__pb2.TimeResponse.SerializeToString,
            ),
            'SyncClocks': grpc.unary_unary_rpc_method_handler(
                    servicer.SyncClocks,
                    request_deserializer=berkeley__pb2.ConnectionRequest.FromString,
                    response_serializer=berkeley__pb2.ConnectionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Berkeley', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Berkeley(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Berkeley/GetTime',
            berkeley__pb2.TimeRequest.SerializeToString,
            berkeley__pb2.TimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SyncClocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Berkeley/SyncClocks',
            berkeley__pb2.ConnectionRequest.SerializeToString,
            berkeley__pb2.ConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
