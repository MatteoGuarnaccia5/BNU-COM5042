import json
import time

from users import User, UserSchema


class SmartHome:
    
    def __init__(self) -> None:
        # self.user_id = None
        self.current_user = User()
        self.user_data: UserSchema | None = None

    def start(self):
        valid_choice = False
        while not valid_choice:
            print('''
            Welcome to the Smart Home App
              1. Login
              2. Sign up
            ''')
            try:
                choice = int(input('Choose option: '))
                if choice == 1:
                    self.login()
                else:
                    self.signUp()
            except:
                continue

    def login(self):
        email = input('Enter your email: ')
        password = input('Enter your passowrd: ')

        try:
            self.user_id = self.current_user.authenticate(email, password)
        except:
            print('Unable to authenticate\n\n')
            time.sleep(2)
            self.start()

        print('Authenticated\n\n')
        time.sleep(1)

        try:
            self.user_data = self.current_user.get(self.user_id)
        except:
            print('Unable to retrieve data')
            # self.create()

        # self.main_menu()


    def signUp(self):

        while True:
            email = input('Enter your email: ')
            password = input('Enter your passowrd: ')
            confirm_password = input('Confirm your password')
            if(password is not confirm_password):
                continue

            # self.create()

        


                