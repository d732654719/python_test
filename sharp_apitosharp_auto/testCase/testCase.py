import unittest

from common.read_ftpfile import read_sa_file
class delivery_test(unittest.TestCase):

    def test_sa(self):
        data_list=read_sa_file()
        assert data_list[0]=="SAHD 00000000     20081812274400000            SHARP                                                                            \n"
        #需要循环断言