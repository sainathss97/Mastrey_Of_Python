import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print("About to test...")

    def test_do_stuff(self):
        '''Test 1'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_2(self):
        '''Test 2'''
        test_param = 'shshjsk'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff_3(self):
        '''Test 3'''
        test_param = 'shshjsk22222'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_4(self):
        '''Test 4'''
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")

    def test_do_stuff_5(self):
        '''Test 5'''
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")

    def tearDown(self):
        print('Cleaning up...')


if __name__ == '__main__':

    unittest.main()
