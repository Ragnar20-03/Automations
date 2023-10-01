import smtplib
import csv



def Send(csvFile):

    sender = "roshanpp20@gmail.com"
    AppPass = "bsxr oiuv chnc osqp"

    s = smtplib.SMTP("smtp.gmail.com" , 587)

    s.starttls()
                    #App Password
    s.login(sender , AppPass)

    message = "An Automated Message From Ragnar20-03"

    for line in csvFile:
        s.sendmail(sender , line[1] , message+"__")


def main():

# Opening Respective CSV File  || With ih used to Execption Handling
    with open ("Demo.csv"  , mode="r") as File:
        
        # Reading csv file
        csvFile = csv.reader(File)

        Send(csvFile)

if __name__== "__main__" :
    main()