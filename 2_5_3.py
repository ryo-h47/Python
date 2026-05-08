import smtplib
import email
import mimetypes
import pandas as pd

server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('your-account@gmail.com','your-password')

folderpath='C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter6//satei'

data=pd.read_excel(folderpath+'//list.xlsx')

for number in range(len(data)):

    To=data.loc[number,'To']

    filename=data.loc[number,'filename']

    filepath=folderpath+'//'+filename

    message=email.message.EmailMessage()

    message['From']='your-account@gmail.com'
    message['To']=To
    message['Subject']='This is a test email'
    message.set_content('This is a test email\nI send this email using Python')

    mimetype=mimetypes.guess_type(filepath)[0]
    mimetype,subtype=mimetype.split('/')

    file=open(filepath,'rb').read()
    message.add_attachment(file,maintype=mimetype,subtype=subtype,filename=filename)

    server.send_message(message)

server.quit()

