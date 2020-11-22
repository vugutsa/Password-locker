import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestCredentials(unittest.TestCase):
    
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
        self.assertEqual(self.new_credentials.handle,"twitter")
        
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the user object is saved into
        the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)
        
         # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("twitter","Melby","6547") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)
        
               # More tests above
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a user from our user list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("twitter","Melby","6547") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting credentials object
            self.assertEqual(len(Credentials.credentials_list),1) 
            
    def test_find_credentials_by_user_name1(self):
        '''
        test to check if we can find credentials by user_name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter","Melby","6547") # new handle
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_user_name1("Melby")

        self.assertEqual(found_credentials,test_credentials) 
if __name__ == '__main__':
    unittest.main()