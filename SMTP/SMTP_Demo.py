import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
        #Username of sender         //App Password
s.login("roshanpp20@gmail.com", "bsxr oiuv chnc osqp")

# message to be sent
message = "An Automated Message from Roshan Patil"

# sending the mail
            # sender                   # Email to send (Reciever)   Messge
s.sendmail("roshanpp20@gmail.com", "r0shanspatilffnis2003@gmail.com",       message)

# terminating the session
s.quit()


#s.login("roshanpp20@gmail.com", "bsxr oiuv chnc osqp")
