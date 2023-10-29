import schedule 
import time 
import datetime 
 
def fun_Minute():
    print("Current time is : ")
    print(datetime.datetime.now())
    print("Schedulat execute after a minute ")

def fun_Hour():
    print("Current time is :")
    print(datetime.datetime.now())
    print("Schedular execute after an hour")

def fun_Day():
    print("Current time is : ")
    print(datetime.datetime.now())
    print("Schedualr executes after day ")

def fun_Afternoon():
    print("Cuurent time is ")
    print(datetime.datetime.now())
    print("Scheduar executes at 12")

def main():
    print("Marvellous InfoSystems : Python Automations & Machine Learning")

    print("Python Job Schedular ")
    print(datetime.datetime.now())

    schedule.every(1).minutes.do(fun_Minute)

    schedule.every().hour.do(fun_Hour)

    schedule.every().day.at("00:00").do(fun_Afternoon)

    schedule.every().sunday.do(fun_Day)

    schedule.every().saturday.at("18:30").do(fun_Day)

    while (True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
