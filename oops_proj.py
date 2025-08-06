

class chatbook:

    __user_id = 100  # static variable to keep track of user IDs

    def __init__(self):
        # Encapsulation:
        # Using private attributes to restrict direct access
        # __name is a private attribute
        self.__name = 'Chatbook'

        # self.id = 0
        # self.id += 1 static var but wrong syntax
        self.id = chatbook.__user_id
        chatbook.__user_id += 1  # Increment static user ID for each new instance

        self.username = ''
        self.password = ''
        self.logged_in = False

        # self.menu()

    # getter and setter methods for private attribute
    # these methods allow controlled access to private attributes
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    # static methods to access and modify static variable
    # static methods are bound to the class and not the instance so not need to pass self
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(id):
        chatbook.__user_id = id    
    
    def menu(self):
        user_input = int(input(("""Welcome to Chatbook!
              1. Signup
              2. Login
              3. Write a post
              4. Message a friend
              Press any other key to exit.\n->""")))
        
        if user_input == 1:
            self.signup()
        elif user_input == 2:
            self.login()
        elif user_input == 3:
            self.my_posts()
        elif user_input == 4:
            self.send_message()
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

    def my_posts(self):
        if self.logged_in:
            print(f"Displaying posts for {self.username}...")
        else:
            print("You need to log in to view posts.")
        print("\n")
        self.menu()
    
    def send_message(self):
        if self.logged_in:
            friend = input("Enter the friend's username: ")
            message = input("Enter your message: ")
            print(f"Message sent to {friend}: {message}")
        else:
            print("You need to log in to send messages.")
        print("\n")
        self.menu()
        


# obj = chatbook()
