import smtplib
import schedule
from sys import *
import csv
import time

def Send():
    s = smtplib.SMTP("smtp.gmail.com" , 587)
    s.starttls()

    s.login("roshanpp20@gmail.com" , "bsxr oiuv chnc osqp" )

    with open("Demo.csv" ) as file :
        csvFile = csv.reader(file)

        headers = next(csvFile)
        print(headers)

        for line in csvFile :
            s.sendmail("roshanpp20@gmail.com" , line[1] , "An Automated Email from RaGnar" )
        
        print("------------------ Mail Succesfully Send ------------------------")

def main():
    print("-----------------------Mail Sender with SMTP-----------------------")
    schedule.every(int(argv[1])).seconds.do(Send)

if __name__=="__main__":
    main()


while (1):
    schedule.run_pending()
    time.sleep(1)