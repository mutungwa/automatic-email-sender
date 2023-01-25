import smtplib
from email.mime.text import MIMEText

# Sender email address and password
sender_email = "sender@example.com"
sender_password = "sender_password"

# Receiver email address
receiver_email = "receiver@example.com"

# Create the message
msg = MIMEText("Hello, this is an automated email.")
msg["Subject"] = "Automated Email"
msg["From"] = sender_email
msg["To"] = receiver_email

# Connect to the server
server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login(sender_email, sender_password)

# Send the email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Close the connection
server.quit()
