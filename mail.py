import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender='maknojiaiman@gmai.com'
	receiver='maknojiaiman@gmail.com'
	msg='hey wassup'
	s.login(maknojiaiman@gmail.com,'password')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("msg sent successfully")
	s.quit()