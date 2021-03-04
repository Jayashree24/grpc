
from __future__ import print_function
import logging

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        while 1:
            num_1 = int(input())
            num_2 = int(input())
            response = stub.CalculateSum(calculator_pb2.SumRequest(first_num=num_1,sec_num=num_2))
            print (response.sum)
            print ('>>>>>')
    #print("Calculator client received: %s" % response.sum)


if __name__ == '__main__':
    logging.basicConfig()
    run()
