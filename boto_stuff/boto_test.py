import boto3
import unittest


class BotoTest(unittest.TestCase):

  def test_version(self):
    self.assertEqual(boto3.__version__, '1.4.7')


if __name__ == '__main__':
  unittest.main()
