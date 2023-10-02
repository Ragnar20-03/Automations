import os
import time
import psutil
import urllib.request as urllib2
import smtplib
import schedule 
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142',timeout = 1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender(filename,time):
    try:
        fromaddr = "shubhamborse0911@gmail.com"
        toaddr = "borse911shubham@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to Marvellous Infosystems.
        Please find attached document which contains Log Running Process.
        Log file is created at : %s

        This is auto generated mail.

        Thanks & Regards,
        Shubham Shyam Borse
        Marvellous Infosystems
          """%(toaddr,time)


        Subject = """
        Marvellous Infosystems Process log generated at : %s
        """%(time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plan'))

        attachment = open(filename,'rb')

        p = MIMEBase('application', 'octet-stream')

        p.se_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename = %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        s.login(fromaddr,"cgxp qnya iogr hgpv")

        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log file succesfully sent through Mail")

    except Exception as E:
        print ("Unable to send mail.",E)

def ProcessLog(log_dir = 'Marvellous'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir,"Marvellous%s.txt"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separator+"\n")
    f.write("Marvellous Infosystems Process Logger : "+time.ctime() + "\n")
    f.write(separator +"\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo);
        except (psutil.NoSuchProcess,psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"% element)

    print("Log file is Succesfully genrated at location %s" % (log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path,time.ctime())
        endTime = time.time()

        print('Took %s Second to send mail'%(endTime - startTime))
    else:
        print("There is no internet Connection")

def main():
    print("---- Marvellous Infosystems by Shubham Borse ----")

    print("Application name : " +argv[0])

    if(len(argv)!= 2):
        print("Error: Invalid number of arguments")
        exit()

    if (argv[1]== "-h" or (argv[1] == "-H")):
        print("This Script is used to Log record of running processes")
        exit()

    if (argv[1]== "-u") or (argv[1]== "-U"):
        print("Usage :ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).seconds.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError as E:
        print("Error : Invalid Datatype of input",E)

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__" :
    main()   