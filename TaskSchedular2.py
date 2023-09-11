import datetime
import schedule
import time

def schedule_minute():
    print("Schedular schedules aftee a minute")
    print("curret time is")
    print(datetime.datetime.now())
    



def main():
    print("Automations in python")
    print(datetime.datetime.now())

    schedule.every(10).seconds.do(schedule_minute)
    
if __name__=="__main__":
    main()


while(True):
    schedule.run_pending()
    time.sleep(1)
