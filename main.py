import time
import uuid
import requests
from datetime import datetime

from schemas.user import UserSchema
from users import User



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
                valid_choice = True
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
            self.create(email, password)

        self.main()


    def signUp(self):

        while True:
            email = input('Enter your email: ')
            password = input('Enter your passowrd: ')
            confirm_password = input('Confirm your password: ')
            if(password != confirm_password):
                print("\n\nPassword do not match")
                continue
            else:
                break
                
        self.create(email, password)

    def create(self, email, password):
        name = input("Enter your name: ")
        user_id = uuid.uuid4().int

        user = UserSchema(
            id=user_id,
            name=name,
            email=email,
            password=password,
            dob=None
        )

        self.current_user.create(user)
        self.user_data = self.current_user.get(user_id)

        self.main()

    def main(self):
        try:
            while True:
                print(
                """
                Main Menu
                1. Emergency Alerts
                2. Energy Efficiency
                """
                )
                try:
                    choice = int(input("\n\nChoose option: "))
                    break
                except:
                    print("\nInvalid choice. Try again.")
                    continue

            print(choice)
        
            if(choice):
                if(choice == 1):
                    self.alert_function_1()

                else:
                    print('Not one of our options. Exiting.')
        except:
            print("Error")

        self.main()
        
  
    def alert_function_1(self):
        print('This is a test simulation of the emergency alert system')

        x = self.alert_function_2()
        while x:
            print('Alert! There is a fire please evacuate')
            time.sleep(5)
            x = self.alert_function_2()
            

    def alert_function_2(self):
        y = requests.get("https://jsonplaceholder.typicode.com/posts")
        if(y.status_code == 200):
            return True
        else:
            return False


if __name__ == "__main__":
    app = SmartHome()
    app.start()   