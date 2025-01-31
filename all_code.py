
# the entire code base that will be used to create PRs etc for the assignment 
import requests
import time

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
    

if __name__ == "__main__":
    send_alert()