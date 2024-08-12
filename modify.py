import email
import smtplib
import imaplib
from email import MIMEText
from email import MIMEMultipart


class Mail:
    def __init__(self, post, password, recipients, message, header, GMAIL_SMTP, GMAIL_IMAP):
        self.post = post
        self.password = password
        self.recipients = recipients
        self.message = message
        self.header = header
        self.GMAIL_IMAP = GMAIL_IMAP
        self.GMAIL_SMTP = GMAIL_SMTP

    def sendMessage(self):
        msg = MIMEMultipart()
        msg['From'] = self.post
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.GMAIL_SMTP, 587) as ms:
            ms.ehlo()
            ms.starttls()
            ms.ehlo()
            ms.login(self.post, self.password)
            ms.sendmail(self.post, msg.as_string())

        return "The message has been sent"

    def recieveMessage(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.post, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)

        if not data[0]:
            return 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == "__main__":
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    post = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None
    amail = Mail(post, password, recipients, message, header, GMAIL_SMTP, GMAIL_IMAP)
    amail.sendMessage()
    amail.recieveMessage()
