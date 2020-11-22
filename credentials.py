class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = [] # Empty credentials list

    def __init__(self,handle,user_name1,password1):

      # docstring removed for simplicity

        self.handle = handle
        self.user_name1 = user_name1
        self.password1 = password1
        
    def save_credentials(self):

        '''
        save_contact method saves contact objects into credentials_list
        '''

        Credentials.credentials_list.append(self)