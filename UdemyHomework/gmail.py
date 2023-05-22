import smtplib
import getpass
#send email
smtp_object = smtplib.SMTP("smtp.gmail.com", 587) #465 # NONE

print(smtp_object.ehlo())
print(smtp_object.starttls())

email = input("Email: ")
paswd = getpass.getpass("Jelszo: ")

smtp_object.login(email, paswd)

from_address = email
to_address = email
subject = input("Adja meg a tárgyat")
massage = input("Adja meg az üzenetet")

msg = "Subject: " + subject + "\n"+massage

smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()

#recive email
import imaplib

M = imaplib.IMAP4_SSL("imap.gmail.com")

email = input("Email: ")
paswd = getpass.getpass("Jelszo: ")

M.login(email, paswd)

print(M.list())

print(M.select('inbox'))

type, data = M.search(None, "SUBJECT 'Bármilehet'") #(None, bármi lehet )

M.quit()