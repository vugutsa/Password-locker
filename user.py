class User:
    """
    Class that generates new instances of contacts
    """
    user_list = [] # Empty user list

    def __init__(self,user_name,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.password = password

        
    def save_user(self):
    
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self) 