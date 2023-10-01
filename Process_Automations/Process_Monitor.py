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
        urllib2.urlopen("http://216.58.192.142" , timeout = 1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender(filename , time):
    try : 
        fromaddr = "roshanpp20@gmail.com"
        toaddr = "r0shanspatilffnis2003@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        body = """
        Hello %s , Welcome to Marvellous Infosystems . 
        Please Find attached document which contains Log of Running Processes.
        Log File is Created at : %s

        This is auto-generated mail.

        Thanks and Regards , 
        Piyush Manohar Khairnar 
        Marvellous Infosystems 
        """%(toaddr , time)

        Subject = """
        Marvellous Infosystems Process Log Generated at : %s
        """ %(time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body , 'plain'))

        attachment = open(filename , "rb")

        p = MIMEBase('application' , 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('COntent-Disposition' , "attachment; filename = %s " %filename)

        msg.attach(p)

        s=smtplib.SMTP('smtp.gmail.com' , 587)

        s.starttls()

        s.login(fromaddr , "bsxr oiuv chnc osqp")

        text = msg.as_string()

        s.sendmail(fromaddr , toaddr , text)
        print("Send Email")

        s.quit()

        print("Log file succesfully sent through Mail")
    except Exception as E :
        print("Unable to send email" , E)
    

def ProcessLog(log_dir = "Marvellous"):
    listprocess=[]
    print("Here")
    if not os.path.exists(log_dir):
        try : 
            os.mkdir(log_dir)
        except :
            pass

    seperator = "-"*80
    log_path = os.path.join(log_dir,"MarvellousLog%s.txt"%(time.ctime()))
    f = open(log_path , "w")
    f.write(seperator + "\n")
    f.write("Marvellous Infosystems Process Logger : " + time.ctime() + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid' , 'name' , 'username'])
            vms = proc.memory_info().vms / (1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess) : 
            pass

    for element in listprocess : 
        f.write("%s\n" %element)
    
    print("Log File is succesfully generated at location %s "  %(log_path))

    connected = is_connected

    if connected : 
        startTime = time.time()
        MailSender(log_path , time.ctime())
        endTime = time.time()

        print("Took %s Seconds to send email " %(endTime - startTime))

    else :
        print("There is no internet connection")
    
def main():
    print("----- Marvellous Infosystems by Roshan Patil -----")
    print("Application name : " +argv[0])

    if (len(argv)!=2):
        print("Error : Invalid number of Arguments ")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Scipt is used to log record of running processes")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U") :
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()
    
    try : 
        schedule.every(int(argv[1])).seconds.do(ProcessLog)
        while True : 
            schedule.run_pending()
            time.sleep(1)
    except  ValueError as V:
        print("Error : Invalid datatype of input" , V)

    except Exception as E :
        print("Error : Invalid Input" , E)


if __name__ == "__main__":
    main()



