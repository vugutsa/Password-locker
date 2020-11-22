import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("twitter","vugutsa","5657") # create credentials object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.user_name1,"vugutsa")
        self.assertEqual(self.new_credentials.password1,"5657")
        
    def test_save_credentials(self):
            '''
        test_save_credentials test case to test if the user object is saved into
        the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)
if __name__ == '__main__':
    unittest.main()