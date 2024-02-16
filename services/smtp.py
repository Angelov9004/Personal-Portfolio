import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Function to send email , it takes user data as an argument and sends email
def send_email(user_data):
    sender_email = os.getenv('SENDER_EMAIL') #sender email, takes it from .env file
    receiver_email = os.getenv('RECEIVER_EMAIL') #receiver email, takes it from .env file
    password = os.getenv('PASSWORD') #password, takes it from .env file

    message = MIMEMultipart() #creating an instance of MIMEMultipart
    message['From'] = sender_email #setting from email
    message['To'] = receiver_email #setting to email
    message['Subject'] = 'Message from your website' #setting subject

    body = f"Name: {user_data['name']}\nEmail: {user_data['email']}\nSubject: {user_data['subject']}\nMessage: {user_data['message']}"
    message.attach(MIMEText(body, 'plain')) #attaching body to message

    server = smtplib.SMTP('smtp.yourserver.com', 25) #creating an instance of SMTP
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()