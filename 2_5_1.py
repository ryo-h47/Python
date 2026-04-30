import smtplib
import email
import mimetypes

server=smtplib.SMTP_SSL('smtp.gmail.com',465)

server.login('your-account@gmail.com','your-password')

message=email.message.EmailMessage()

message['From']='your-account@gmail.com'
message['To']='receiver-account@gmail.com'
message['Subject']='This is a test email'
message.set_content('This is a test email\nI send this email using Python')

server.send_message(message)

server.quit()