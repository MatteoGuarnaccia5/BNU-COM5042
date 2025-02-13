
# the entire code base that will be used to create PRs etc for the assignment 
import requests
import time
from datetime import datetime

# emergency alert
def send_alert():

    
    fire_alarm_active = get_alarm_status()
    while fire_alarm_active:
        print('Alert! There is a fire please evacuate')
        time.sleep(5)
        fire_alarm_active = get_alarm_status()
        



def get_alarm_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if(response.status_code == 200):
        return True
    else:
        return False


# energy efficiency
def pick_appliance():
    print("""
        What appliance would you like to schedule?
          1. Thermostat
          2. Lighting
          3. Other smart
        """)
    user_input = input("Please enter a number ")
    try:
        choice = int(user_input)
    except:
        print('Not valid input')
        return

    if(choice == 1):
        temp = int(input('What temperature would you like to set? '))
        date_string = input('When would you like to schedule this change? (dd/mm/yyyy hh:mm) Or enter for right now')
        date = datetime.now()
        if(date_string != ''):
            date = datetime.strptime(date_string, '%d %m %y %h %m')
        time.sleep(1)
        print(f'Setting thermostat to {temp} on {date}')

    elif(choice == 2):
        lights = input('What lights would you like turned on? ')
        off_lights = input('What lights would you like turned off? ')

        print(f'Turning on {lights} and turning off {off_lights}')
    
    else:
        des = input('Please describe what you would like to do ')
        print('Tasks completed')


if __name__ == "__main__":
    # emergency alert
    # send_alert()

    #energy efficiency
    pick_appliance()
