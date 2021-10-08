import smtplib

to =  input("Enter the email of reciver")

content = input("Enter the content of email")

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # 587 is the port number of gmail 
    server.ehlo() # i thing this wil connect to server
    server.starttls()
    server.login('youremail address', 'your pswd')
    #loging in using gmail account
    server.sendmail('your emsil id', to ,content)
    #Sending email
    server.close

sendemail(to, content)
    