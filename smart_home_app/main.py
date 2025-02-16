"""Root of the Smart Home App"""

import time
import uuid
from datetime import datetime

import requests

from smart_home_app.schemas.user import UserSchema
from smart_home_app.users import User


class SmartHome:
    """THe SmartHomeApp class"""

    def __init__(self) -> None:
        self.current_user = User()
        self.user_data: UserSchema | None = None

    def start(self):
        """Root of the app"""
        valid_choice = False
        while not valid_choice:
            print(
                """
            Welcome to the Smart Home App
              1. Login
              2. Sign up
            """
            )
            try:
                choice = int(input("Choose option: "))
                valid_choice = True
                if choice == 1:
                    self.login()
                elif choice == 2:
                    self.sign_up()
                else:
                    raise SystemExit("Invalid Option Error")
            except ValueError:
                continue

    def login(self):
        """Log user in"""
        email = input("Enter your email: ")
        password = input("Enter your passowrd: ")

        try:
            user_id = self.current_user.authenticate(email, password)
        except ValueError:
            print("Unable to authenticate\n\n")
            time.sleep(2)
            self.start()

        print("Authenticated\n\n")
        time.sleep(1)

        try:
            self.user_data = self.current_user.get(user_id)
        except ValueError:
            print("Unable to retrieve data")
            self.create(email, password)

        self.main()

    def sign_up(self):
        """Method to sign up new user"""

        while True:
            email = input("Enter your email: ")
            password = input("Enter your passowrd: ")
            confirm_password = input("Confirm your password: ")
            if password != confirm_password:
                print("\n\nPassword do not match")
                continue

            try:
                self.create(email, password)
            except ValueError:
                print("User already exists, please login.")
                self.start()

            break

    def create(self, email, password):
        """Create new user document"""
        name = input("Enter your name: ")
        user_id = uuid.uuid4().int

        user = UserSchema(
            id=user_id, name=name, email=email, password=password, dob=None
        )

        self.current_user.create(user)
        self.user_data = self.current_user.get(user_id)

        self.main()

    def main(self):
        """Main menu of the app"""
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
                except TypeError:
                    print("\nInvalid choice. Try again.")
                    continue

            if choice == 1:
                self.send_alert()
            elif choice == 2:
                self.pick_appliance()
            else:
                print("Not one of our options. Exiting.")
        except TypeError:
            print("Invalid input. Please try again")

        self.main()

    def send_alert(self):
        """Send emergency alert"""
        print("This is a test simulation of the emergency alert system")

        fire_alarm_active = self.get_alarm_status()
        while fire_alarm_active:
            print("Alert! There is a fire please evacuate")
            time.sleep(5)
            fire_alarm_active = self.get_alarm_status()

    def get_alarm_status(self):
        """Get the fire alarm status"""
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts", timeout=200
        )
        return response.status_code == 200

    def pick_appliance(self):
        """Pick smart appliance"""
        while True:
            print(
                """
            What appliance would you like to schedule?
            1. Thermostat
            2. Lighting
            3. Other smart
            """
            )
            user_input = input("Please enter a number ")
            try:
                choice = int(user_input)
                break
            except TypeError:
                print("Not valid input")
                continue

        if choice == 1:
            self.manage_thermostat()

        elif choice == 2:
            self.manage_lights()

        else:
            des = input("Please describe what you would like to do ")
            print(f"Completing: ${des}")
            time.sleep(1)
            print("\nTasks completed")

    def manage_thermostat(self):
        """Manage thermostat"""
        temp = int(input("What temperature would you like to set? "))
        date_string = input(
            """When would you like to schedule this change?
                            (dd/mm/yyyy hh:mm) Or enter for right now"""
        )
        date = datetime.now()
        if date_string != "":
            date = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
        time.sleep(1)
        print(f"\nSetting thermostat to {temp} on {date}")

    def manage_lights(self):
        """Manage lights"""
        lights = input("What lights would you like turned on? ")
        off_lights = input("What lights would you like turned off? ")
        print(f"Turning on {lights} and turning off {off_lights}")


if __name__ == "__main__":
    app = SmartHome()
    app.start()
