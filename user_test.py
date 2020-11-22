import unittest # Importing the unittest module
from user import User # Importing the user class

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
        self.new_user = User("vugutsa","5657") # create user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"vugutsa")
        self.assertEqual(self.new_user.password,"5657")
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

  # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []


    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Bella","6579") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
        
        # More tests above
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Bella","6579") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)
            
    def test_find_user_by_user_name(self):
            '''
            test to check if we can find a contact by phone number and display information
            '''

            self.new_user.save_user()
            test_user = User("Bella","6579") # new user
            test_user.save_user()

            found_user = User.find_by_user_name("Bella")

            self.assertEqual(found_user,test_user) 
            
    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("Bella","6579") # new contact
        test_user.save_user()

        user_exists = User.user_exist("Bella")

        self.assertTrue(user_exists)
if __name__ == '__main__':
    unittest.main()