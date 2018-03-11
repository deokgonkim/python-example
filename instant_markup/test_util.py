import unittest

class test_util(unittest.TestCase):

    def testLines(self):
        pass
        from util import lines
        f = open('test_input.txt')
        try:
            for line, item in enumerate(lines(f)):
                print('%d\t %s' % (line, item)) 
        finally:
            f.close()
        print("test")
        self.failUnless(1 == 1, "Failed")

    def testBlocks(self):
        from util import blocks
        f = open('test_input.txt')
        try:
            for line, item in enumerate(blocks(f)):
                print('block %d\t %s' % (line, item)) 
        finally:
            f.close()
        print("test")
        self.failUnless(1 == 1, "Failed")


if __name__ == '__main__':
    unittest.main()
