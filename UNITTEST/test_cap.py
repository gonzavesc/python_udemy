import unittest
import cap

class test_cap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap(text)
        self.assertEqual(result,'Python')
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap(text)
        self.assertEqual(result,'Monty Python')
if __name__=='__main__':
    unittest.main()