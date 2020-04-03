# Google Search Results Scraper
# make sure to install the following libraries:
# pip install beautifulsoup4
# pip install google
import numpy as np

count = 0
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
#query = input('what do you want to search?: ')
#result = input('what is the max number of search results?: ')
#resultnum = int(result)
query = input('what do you want to search?: ')
res = input('what is the max number of search results?: ')
maxresults = int(res)
fname = input('what is the name of the excel file?: ')
password = input("Type your password and press enter: ")

word = query.split()
print(word)

lst = list()
count = 0
results = 0
for i in word:
	for j in search(word[count], tld="com", num=maxresults, stop=maxresults, pause=3):
		lst.append(j)
		results = results + 1
		print(j)

	print('"'+word[count]+'" search results:', results)
	results = 0
	count = count + 1
	continue
print(lst)

arr = np.array(lst)
# Save Numpy array to csv
np.savetxt(fname, arr, delimiter =",", fmt = "%s")

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "jmzakatees@gmail.com"  # Enter your address
#receiver_email = input("What is the recipient email address?: ")  # Enter receiver address
receiver_email = "jsiddique@gmail.com"
#subj = input("What is the subject of the email?: ")
subj = "testing attachments"
#txtwords = input('what do you want to say?: ')
body = "This is an email with attachment sent from Python"


message = MIMEMultipart()
message["Subject"] = subj
message["From"] = sender_email
message["To"] = receiver_email

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = fname  # In same directory as script

with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
