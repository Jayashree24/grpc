
from __future__ import print_function
import logging

import grpc

import primenumber_pb2
import primenumber_pb2_grpc
import time


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = primenumber_pb2_grpc.PrimeDecompositionStub(channel)
        while 1:
                num = int(input())
                response = stub.PrimeNumber(primenumber_pb2.PrimeRequest(num=num))
                i = 1
                for r in response:
                    print (r.factor)
                    time.sleep(1)
                    i += 1
                print ('*****')
    #print("Calculator client received: %s" % response.sum)


if __name__ == '__main__':
    logging.basicConfig()
    run()
