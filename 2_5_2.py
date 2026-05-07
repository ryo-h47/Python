import mimetypes
import email
import smtplib

server=smtplib.SMTP_SSL('smtp.gmail.com',465)

message=email.message.EmailMessage()

mimetype=mimetypes.guess_type('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter6//sample.xlsx')[0]

print(mimetype)

mimetype,subtype=mimetype.split('/')

print(mimetype)
print(subtype)

file=open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter6//sample.xlsx','rb').read()

message.add_attachment(file,maintype=mimetype,subtype=subtype,filename='sample.xlsx')

server.send_message(message)

server.quit()