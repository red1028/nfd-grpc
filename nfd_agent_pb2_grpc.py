<<<<<<< HEAD
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import nfd_agent_pb2 as nfd__agent__pb2


class NFDRouterAgentStub(object):
    """NFD and NLSR exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NFDHostNotify = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDHostNotify',
                request_serializer=nfd__agent__pb2.NFDHost.SerializeToString,
                response_deserializer=nfd__agent__pb2.AckReply.FromString,
                )
        self.NFDFaceList = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDFaceList',
                request_serializer=nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.NFDFaceListRes.FromString,
                )
        self.NFDFaceCreate = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDFaceCreate',
                request_serializer=nfd__agent__pb2.NFDFaceCreateReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.AckReply.FromString,
                )
        self.NFDFaceDestroy = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDFaceDestroy',
                request_serializer=nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.AckReply.FromString,
                )
        self.NFDFibList = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDFibList',
                request_serializer=nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.NFDFibListRes.FromString,
                )
        self.NFDRouteList = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDRouteList',
                request_serializer=nfd__agent__pb2.NFDRouteListReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.NFDRouteListRes.FromString,
                )
        self.NFDRouteShow = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDRouteShow',
                request_serializer=nfd__agent__pb2.NFDRouteShowReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.NFDRouteShowRes.FromString,
                )
        self.NFDRouteAdd = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDRouteAdd',
                request_serializer=nfd__agent__pb2.NFDRouteReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.AckReply.FromString,
                )
        self.NFDRouteRemove = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDRouteRemove',
                request_serializer=nfd__agent__pb2.NFDRouteReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.AckReply.FromString,
                )
        self.NFDStatusReport = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDStatusReport',
                request_serializer=nfd__agent__pb2.NFDStatusReportReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.NFDStatusReportRes.FromString,
                )
        self.NFDStrategyList = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDStrategyList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=nfd__agent__pb2.NFDStrategyListRes.FromString,
                )
        self.NFDStrategyShow = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDStrategyShow',
                request_serializer=nfd__agent__pb2.NFDStrategyReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.NFDStrategyShowRes.FromString,
                )
        self.NFDStrategySet = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDStrategySet',
                request_serializer=nfd__agent__pb2.NFDStrategyReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.AckReply.FromString,
                )
        self.NFDStrategyUnset = channel.unary_unary(
                '/nfd.NFDRouterAgent/NFDStrategyUnset',
                request_serializer=nfd__agent__pb2.NFDStrategyReq.SerializeToString,
                response_deserializer=nfd__agent__pb2.AckReply.FromString,
                )


class NFDRouterAgentServicer(object):
    """NFD and NLSR exported by the server.
    """

    def NFDHostNotify(self, request, context):
        """A agent-to-external
        Advertisement NFD Infomation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDFaceList(self, request, context):
        """A external-to-agent
        face command
        rpc NFDFaceList(NFDFaceIDReq) returns (stream NFDFaceListRes) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDFaceCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDFaceDestroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDFibList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDRouteList(self, request, context):
        """route command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDRouteShow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDRouteAdd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDRouteRemove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDStatusReport(self, request, context):
        """status command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDStrategyList(self, request, context):
        """strategy command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDStrategyShow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDStrategySet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFDStrategyUnset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NFDRouterAgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NFDHostNotify': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDHostNotify,
                    request_deserializer=nfd__agent__pb2.NFDHost.FromString,
                    response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
            ),
            'NFDFaceList': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDFaceList,
                    request_deserializer=nfd__agent__pb2.NFDFaceIDReq.FromString,
                    response_serializer=nfd__agent__pb2.NFDFaceListRes.SerializeToString,
            ),
            'NFDFaceCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDFaceCreate,
                    request_deserializer=nfd__agent__pb2.NFDFaceCreateReq.FromString,
                    response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
            ),
            'NFDFaceDestroy': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDFaceDestroy,
                    request_deserializer=nfd__agent__pb2.NFDFaceIDReq.FromString,
                    response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
            ),
            'NFDFibList': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDFibList,
                    request_deserializer=nfd__agent__pb2.NFDFaceIDReq.FromString,
                    response_serializer=nfd__agent__pb2.NFDFibListRes.SerializeToString,
            ),
            'NFDRouteList': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDRouteList,
                    request_deserializer=nfd__agent__pb2.NFDRouteListReq.FromString,
                    response_serializer=nfd__agent__pb2.NFDRouteListRes.SerializeToString,
            ),
            'NFDRouteShow': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDRouteShow,
                    request_deserializer=nfd__agent__pb2.NFDRouteShowReq.FromString,
                    response_serializer=nfd__agent__pb2.NFDRouteShowRes.SerializeToString,
            ),
            'NFDRouteAdd': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDRouteAdd,
                    request_deserializer=nfd__agent__pb2.NFDRouteReq.FromString,
                    response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
            ),
            'NFDRouteRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDRouteRemove,
                    request_deserializer=nfd__agent__pb2.NFDRouteReq.FromString,
                    response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
            ),
            'NFDStatusReport': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDStatusReport,
                    request_deserializer=nfd__agent__pb2.NFDStatusReportReq.FromString,
                    response_serializer=nfd__agent__pb2.NFDStatusReportRes.SerializeToString,
            ),
            'NFDStrategyList': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDStrategyList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=nfd__agent__pb2.NFDStrategyListRes.SerializeToString,
            ),
            'NFDStrategyShow': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDStrategyShow,
                    request_deserializer=nfd__agent__pb2.NFDStrategyReq.FromString,
                    response_serializer=nfd__agent__pb2.NFDStrategyShowRes.SerializeToString,
            ),
            'NFDStrategySet': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDStrategySet,
                    request_deserializer=nfd__agent__pb2.NFDStrategyReq.FromString,
                    response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
            ),
            'NFDStrategyUnset': grpc.unary_unary_rpc_method_handler(
                    servicer.NFDStrategyUnset,
                    request_deserializer=nfd__agent__pb2.NFDStrategyReq.FromString,
                    response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nfd.NFDRouterAgent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NFDRouterAgent(object):
    """NFD and NLSR exported by the server.
    """

    @staticmethod
    def NFDHostNotify(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDHostNotify',
            nfd__agent__pb2.NFDHost.SerializeToString,
            nfd__agent__pb2.AckReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDFaceList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDFaceList',
            nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
            nfd__agent__pb2.NFDFaceListRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDFaceCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDFaceCreate',
            nfd__agent__pb2.NFDFaceCreateReq.SerializeToString,
            nfd__agent__pb2.AckReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDFaceDestroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDFaceDestroy',
            nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
            nfd__agent__pb2.AckReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDFibList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDFibList',
            nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
            nfd__agent__pb2.NFDFibListRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDRouteList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDRouteList',
            nfd__agent__pb2.NFDRouteListReq.SerializeToString,
            nfd__agent__pb2.NFDRouteListRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDRouteShow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDRouteShow',
            nfd__agent__pb2.NFDRouteShowReq.SerializeToString,
            nfd__agent__pb2.NFDRouteShowRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDRouteAdd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDRouteAdd',
            nfd__agent__pb2.NFDRouteReq.SerializeToString,
            nfd__agent__pb2.AckReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDRouteRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDRouteRemove',
            nfd__agent__pb2.NFDRouteReq.SerializeToString,
            nfd__agent__pb2.AckReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDStatusReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDStatusReport',
            nfd__agent__pb2.NFDStatusReportReq.SerializeToString,
            nfd__agent__pb2.NFDStatusReportRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDStrategyList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDStrategyList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            nfd__agent__pb2.NFDStrategyListRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDStrategyShow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDStrategyShow',
            nfd__agent__pb2.NFDStrategyReq.SerializeToString,
            nfd__agent__pb2.NFDStrategyShowRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDStrategySet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDStrategySet',
            nfd__agent__pb2.NFDStrategyReq.SerializeToString,
            nfd__agent__pb2.AckReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFDStrategyUnset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nfd.NFDRouterAgent/NFDStrategyUnset',
            nfd__agent__pb2.NFDStrategyReq.SerializeToString,
            nfd__agent__pb2.AckReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
=======
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT! 
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import nfd_agent_pb2 as nfd__agent__pb2


class NFDRouterAgentStub(object):
  """NFD and NLSR exported by the server.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NFDHostNotify = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDHostNotify',
        request_serializer=nfd__agent__pb2.NFDHost.SerializeToString,
        response_deserializer=nfd__agent__pb2.AckReply.FromString,
        )
    self.NFDFaceList = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDFaceList',
        request_serializer=nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.NFDFaceListRes.FromString,
        )
    self.NFDFaceCreate = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDFaceCreate',
        request_serializer=nfd__agent__pb2.NFDFaceCreateReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.AckReply.FromString,
        )
    self.NFDFaceDestroy = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDFaceDestroy',
        request_serializer=nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.AckReply.FromString,
        )
    self.NFDFibList = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDFibList',
        request_serializer=nfd__agent__pb2.NFDFaceIDReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.NFDFibListRes.FromString,
        )
    self.NFDRouteList = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDRouteList',
        request_serializer=nfd__agent__pb2.NFDRouteListReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.NFDRouteListRes.FromString,
        )
    self.NFDRouteShow = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDRouteShow',
        request_serializer=nfd__agent__pb2.NFDRouteShowReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.NFDRouteShowRes.FromString,
        )
    self.NFDRouteAdd = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDRouteAdd',
        request_serializer=nfd__agent__pb2.NFDRouteReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.AckReply.FromString,
        )
    self.NFDRouteRemove = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDRouteRemove',
        request_serializer=nfd__agent__pb2.NFDRouteReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.AckReply.FromString,
        )
    self.NFDStatusReport = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDStatusReport',
        request_serializer=nfd__agent__pb2.NFDStatusReportReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.NFDStatusReportRes.FromString,
        )
    self.NFDStrategyList = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDStrategyList',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=nfd__agent__pb2.NFDStrategyListRes.FromString,
        )
    self.NFDStrategyShow = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDStrategyShow',
        request_serializer=nfd__agent__pb2.NFDStrategyReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.NFDStrategyShowRes.FromString,
        )
    self.NFDStrategySet = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDStrategySet',
        request_serializer=nfd__agent__pb2.NFDStrategyReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.AckReply.FromString,
        )
    self.NFDStrategyUnset = channel.unary_unary(
        '/nfd.NFDRouterAgent/NFDStrategyUnset',
        request_serializer=nfd__agent__pb2.NFDStrategyReq.SerializeToString,
        response_deserializer=nfd__agent__pb2.AckReply.FromString,
        )


class NFDRouterAgentServicer(object):
  """NFD and NLSR exported by the server.
  """

  def NFDHostNotify(self, request, context):
    """A agent-to-external
    Advertisement NFD Infomation
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDFaceList(self, request, context):
    """A external-to-agent
    face command
    rpc NFDFaceList(NFDFaceIDReq) returns (stream NFDFaceListRes) {}
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDFaceCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDFaceDestroy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDFibList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDRouteList(self, request, context):
    """route command
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDRouteShow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDRouteAdd(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDRouteRemove(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDStatusReport(self, request, context):
    """status command
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDStrategyList(self, request, context):
    """strategy command
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDStrategyShow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDStrategySet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NFDStrategyUnset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NFDRouterAgentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NFDHostNotify': grpc.unary_unary_rpc_method_handler(
          servicer.NFDHostNotify,
          request_deserializer=nfd__agent__pb2.NFDHost.FromString,
          response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
      ),
      'NFDFaceList': grpc.unary_unary_rpc_method_handler(
          servicer.NFDFaceList,
          request_deserializer=nfd__agent__pb2.NFDFaceIDReq.FromString,
          response_serializer=nfd__agent__pb2.NFDFaceListRes.SerializeToString,
      ),
      'NFDFaceCreate': grpc.unary_unary_rpc_method_handler(
          servicer.NFDFaceCreate,
          request_deserializer=nfd__agent__pb2.NFDFaceCreateReq.FromString,
          response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
      ),
      'NFDFaceDestroy': grpc.unary_unary_rpc_method_handler(
          servicer.NFDFaceDestroy,
          request_deserializer=nfd__agent__pb2.NFDFaceIDReq.FromString,
          response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
      ),
      'NFDFibList': grpc.unary_unary_rpc_method_handler(
          servicer.NFDFibList,
          request_deserializer=nfd__agent__pb2.NFDFaceIDReq.FromString,
          response_serializer=nfd__agent__pb2.NFDFibListRes.SerializeToString,
      ),
      'NFDRouteList': grpc.unary_unary_rpc_method_handler(
          servicer.NFDRouteList,
          request_deserializer=nfd__agent__pb2.NFDRouteListReq.FromString,
          response_serializer=nfd__agent__pb2.NFDRouteListRes.SerializeToString,
      ),
      'NFDRouteShow': grpc.unary_unary_rpc_method_handler(
          servicer.NFDRouteShow,
          request_deserializer=nfd__agent__pb2.NFDRouteShowReq.FromString,
          response_serializer=nfd__agent__pb2.NFDRouteShowRes.SerializeToString,
      ),
      'NFDRouteAdd': grpc.unary_unary_rpc_method_handler(
          servicer.NFDRouteAdd,
          request_deserializer=nfd__agent__pb2.NFDRouteReq.FromString,
          response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
      ),
      'NFDRouteRemove': grpc.unary_unary_rpc_method_handler(
          servicer.NFDRouteRemove,
          request_deserializer=nfd__agent__pb2.NFDRouteReq.FromString,
          response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
      ),
      'NFDStatusReport': grpc.unary_unary_rpc_method_handler(
          servicer.NFDStatusReport,
          request_deserializer=nfd__agent__pb2.NFDStatusReportReq.FromString,
          response_serializer=nfd__agent__pb2.NFDStatusReportRes.SerializeToString,
      ),
      'NFDStrategyList': grpc.unary_unary_rpc_method_handler(
          servicer.NFDStrategyList,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=nfd__agent__pb2.NFDStrategyListRes.SerializeToString,
      ),
      'NFDStrategyShow': grpc.unary_unary_rpc_method_handler(
          servicer.NFDStrategyShow,
          request_deserializer=nfd__agent__pb2.NFDStrategyReq.FromString,
          response_serializer=nfd__agent__pb2.NFDStrategyShowRes.SerializeToString,
      ),
      'NFDStrategySet': grpc.unary_unary_rpc_method_handler(
          servicer.NFDStrategySet,
          request_deserializer=nfd__agent__pb2.NFDStrategyReq.FromString,
          response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
      ),
      'NFDStrategyUnset': grpc.unary_unary_rpc_method_handler(
          servicer.NFDStrategyUnset,
          request_deserializer=nfd__agent__pb2.NFDStrategyReq.FromString,
          response_serializer=nfd__agent__pb2.AckReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nfd.NFDRouterAgent', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
>>>>>>> 7874f50eec1c6b3a81c33c65700fbfdb578fab96
