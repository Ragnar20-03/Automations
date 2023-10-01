import smtplib
import pandas

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("roshanpp20@gmail.com", "bsxr oiuv chnc osqp")

# message to be sent
message = "An Automated Message from Roshan Patil"

# sending the mail
s.sendmail("roshanpp20@gmail.com", "", message)

# terminating the session
s.quit()


#s.login("roshanpp20@gmail.com", "bsxr oiuv chnc osqp")
