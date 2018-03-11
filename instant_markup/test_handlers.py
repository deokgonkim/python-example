import unittest

class test_handlers(unittest.TestCase):

    def test_sub(self):
        from handlers import HTMLRenderer
        import re

        handler = HTMLRenderer()
        text_input = 'This *is* a test'
        expected_text = 'This <em>is</em> a test'
        
        result_text = re.sub('\*(.+?)\*', handler.sub('emphasis'), text_input)

        self.failUnless(result_text == expected_text, "Didn't got expected Text")


if __name__ == '__main__':
    unittest.main()
