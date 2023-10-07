import smtplib

s = smtplib.SMTP("smtp.gmail.com" , 587)

s.starttls()

s.login("roshanpp20@gmail.com" , "bsxr oiuv chnc osqp")

s.sendmail("roshanpp20@gmail.com" , "r0shanspatilffnis2003@gmail.com"  , "Hiiiiiii")
print("Send mail success")
s.quit()

