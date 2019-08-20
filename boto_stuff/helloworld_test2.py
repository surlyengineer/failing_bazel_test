import unittest

from boto_stuff import helloworld


class HelloWorldTest(unittest.TestCase):

  def test_helloworld(self):
    hw = helloworld.HelloWorld()
    hw.SayHello()

  def test_helloworld_async(self):
    hw = helloworld.HelloWorld()
    hw.SayHelloAsync()
    hw.Stop()

  def test_helloworld_multiple(self):
    hw = helloworld.HelloWorld()
    hw.SayHelloAsync()
    hw.SayHelloAsync()
    hw.SayHelloAsync()
    hw.SayHelloAsync()
    hw.Stop()


if __name__ == '__main__':
  unittest.main()
