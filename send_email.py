import smtplib

# Creating Send email class
class Send_email:

    def __init__(self, subject, body, recipient):  
        self.subject = subject
        self.body = body
        self.recipient = recipient
    
    # Methode to send an email
    def sent(self):
        user='python.instruction@gmail.com' # From
        pwd="*********" # Password
        recipient = self.recipient
        FROM=user
        TO = [recipient]
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), self.subject, self.body)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('Email sent!')
        
        except:
            print('Something went wrong...')

if __name__ == "__main__":
    # Taking Inputs from User
    subject = input("Subject ? ")
    body = input("Body? ")
    recipient = input("Recipient? ")
    snt=Send_email(subject, body, recipient)
    snt.sent()