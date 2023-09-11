import datetime
import schedule


def schedule_job():
    print("Drink Water please")

schedule.every(1).hour.do(schedule_job)

while(True):
    schedule.run_pending()
