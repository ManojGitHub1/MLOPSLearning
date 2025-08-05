class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.logged_in = False

        self.menu()
    
    def menu(self):
        user_input = int(input((""" Welcome to Chatbook!
              1. Signup
              2. Login
              3. Write a post
              4. Message a friend
              Press any other key to exit.""")))
        
        
        if user_input == '1':
            self.login()
        elif user_input == '2':
            self.register()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()


obj = chatbook()