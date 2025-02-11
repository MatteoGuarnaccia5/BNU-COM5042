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

        if(choice == 2):
            self.pick_appliance()
        else:
            print('Not one of our options. Exiting.')

        self.main()
  

    def pick_appliance(self):
        
        while True:
            print("""
            What appliance would you like to schedule?
            1. Thermostat
            2. Lighting
            3. Other smart
            """)
            user_input = input("Please enter a number ")
            try:
                choice = int(user_input)
                break
            except:
                print('Not valid input')
                continue

        if(choice == 1):
            temp = int(input('What temperature would you like to set? '))
            date_string = input('When would you like to schedule this change? (dd/mm/yyyy hh:mm) Or enter for right now')
            date = datetime.now()
            if(date_string != ''):
                date = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
            time.sleep(1)
            print(f'\nSetting thermostat to {temp} on {date}')

        elif(choice == 2):
            lights = input('What lights would you like turned on? ')
            off_lights = input('What lights would you like turned off? ')

            print(f'Turning on {lights} and turning off {off_lights}')
    
        else:
            des = input('Please describe what you would like to do ')
            print(f"Completing: ${des}")
            time.sleep(1)
            print('\nTasks completed') 




            

if __name__ == "__main__":
    app = SmartHome()
    app.start()   