import smtplib
def send_message(message):
   s = smtplib.SMTP('mail.yourisp.com')
   s.sendmail(
        message['From'],
        message['To'],
        message.as_string())
   s.close()

if __name__ == '__main__':
   email = mail_report('brandonchamba@gmail.com','GOOG')
   send_message(email)
