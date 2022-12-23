import parse
from Lab7 import *

class TestSuite():
    def test_something(self):
        result, error = client()
        result = result.decode('utf-8')

        print('     > received from fixture client is: \n{}'.format(result))
        assert not error
        print(type(result))
        dict = parse(result)
        print(dict)
        for value in dict:
            assert value['Transfer']>1

#TestSuite().test_something(client())