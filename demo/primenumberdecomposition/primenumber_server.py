from concurrent import futures
import logging

import grpc

import primenumber_pb2
import primenumber_pb2_grpc


class PrimeDecomposer(primenumber_pb2_grpc.PrimeDecompositionServicer):

    def PrimeNumber(self, request, context):
        k = 2
        N = request.num
        print ("PrimeDecomposer server received number %s" % N) 
        while N > 1:
           if (N % k) == 0:   
               #print (k)
               yield primenumber_pb2.PrimeReply(factor=k)      
               N = N / k    
           else:
               k = k + 1

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    primenumber_pb2_grpc.add_PrimeDecompositionServicer_to_server(PrimeDecomposer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
