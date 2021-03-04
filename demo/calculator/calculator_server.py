from concurrent import futures
import logging

import grpc

import calculator_pb2
import calculator_pb2_grpc


class Calculator(calculator_pb2_grpc.CalculatorServicer):

    def CalculateSum(self, request, context):
        print ('Calculator server received %s, %s' % (request.first_num, request.sec_num))
        return calculator_pb2.SumReply(sum=request.first_num+request.sec_num)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
