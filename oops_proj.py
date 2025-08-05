class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.logged_in = False

        self.menu()
    
    def menu(self):
        user_input = int(input(("""Welcome to Chatbook!
              1. Signup
              2. Login
              3. Write a post
              4. Message a friend
              Press any other key to exit.\n""")))
        
        if user_input == 1:
            self.signup()
        elif user_input == 2:
            self.login()
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        else:
            exit()

    def signup(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print(f"User {self.username} signed up successfully!")
        print("\n")
        self.menu()

    def login(self):
        if self.username and self.password:
            print(f"User {self.username} logged in successfully!\n")
            self.logged_in = True
        else:
            print("Please sign up first.")
            self.signup()
        print("\n")
        self.menu()
        


obj = chatbook()
