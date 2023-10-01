import smtplib
import schedule
from sys import *
import time

def Send():

    list_emails = ["r0shanspatilffnis2003@gmail.com" , "ap7827681@gmail.com" , "r0shanspatilgp@gmil.com" , "patilpg66@gmail.com"]
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    try:
        s.login("roshanpp20@gmail.com", "bsxr oiuv chnc osqp")
    except Exception as E :
        print("E" , E)
    # message to be sent
    message = """Its Been 1 Hour , Please Drink Water! 
                Have A Good Day !!!
                """

    # sending the mail
    try:
        for email in list_emails :
            i = 1 ; 
            print(i)
            s.sendmail("roshanpp20@gmail.com" , email , message)
            i = i+1
    except Exception as E :
        print("X" , E)


    # terminating the session
    s.quit()
    

def main():
    schedule.every(int(argv[1])).seconds.do(Send)


if __name__ == "__main__":
    main()

while (1):
    schedule.run_pending()
    time.sleep(1)

# ap7827681@gmail.com
