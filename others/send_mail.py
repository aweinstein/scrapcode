import getpass
import smtplib
from email.mime.text import MIMEText


def send_mail(toaddrs='alejandro.weinstein@gmail.com',
              msg_txt='This is just a text message',
              subject='Test message (from Python script!)'):
    fromaddr = 'alejandro.weinstein@gmail.com'
    #toaddrs  = 'alejandro.weinstein@gmail.com'
    msg = MIMEText(msg_txt)
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Subject'] = subject

    # Credentials (if needed)
    username = raw_input('Enter username: ')
    password = getpass.getpass()

    # The actual mail send
    print 'Sending mail'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()
    print 'Done'

if __name__ == '__main__':
    send_mail()
