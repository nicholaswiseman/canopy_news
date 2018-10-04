import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(fromaddr,password,toaddr,subject,body):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject
	msg.attach(MIMEText(body,'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	#Next, log in to the server
	server.login(fromaddr, password)

	#Send the mail
	mail = msg.as_string()
	server.sendmail(fromaddr, toaddr, mail)

if __name__ == '__main__':	
	send_email('canopy.updates@gmail.com','nickandjosh','njww06@mun.ca','test sub','test body')