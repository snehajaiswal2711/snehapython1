#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("sneha.jaiswal2702@gmail.com","93698509332711")
msg="hey there"
server.sendmail("sneha.jaiswal2702@gmail.com","sneha.jaiswal2702@gmail.com",msg)
print("success")
server.quit()