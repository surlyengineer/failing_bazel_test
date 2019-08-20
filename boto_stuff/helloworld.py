from concurrent import futures
import boto3


class HelloWorld(object):
  def __init__(self):
    self._threadpool = futures.ThreadPoolExecutor(max_workers=5)

  def SayHello(self):
    print("Hello World")

  def SayHelloAsync(self):
    self._threadpool.submit(self.SayHello)

  def Stop(self):
    self._threadpool.shutdown(wait = True)

