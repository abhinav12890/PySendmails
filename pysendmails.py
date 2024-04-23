import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('abhinavkumarpal890@gmail.com','dlclytxdhhhvuzmb')
# gmail app password= dlclytxdhhhvuzmb
subject = "test python"
body = " Python programming"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ['assassin2624@gmail.com']
ob.sendmail('abhinavkumarpal890@gmail.com', listadd, message)
print("send mail")
ob.quit()
