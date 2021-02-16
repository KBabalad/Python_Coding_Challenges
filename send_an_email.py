"""
This program is a useful, if you are doing anaysis of large amount of data and you need an notification to be sent to you
when the analyses of this data is complete Or can be a used as a security if someone logs in to your account unauthorised
you can send an email to your account.
"""

import smtplib

my_user_name = 'karanbabalad2@gmail.com'
my_password = 'Kar.890ran'

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server: # using a smtp servers to connect to google to send an email not a secure thing to do, If you have a dummy gmail account use it.
        server.login(my_user_name,my_password)
        server.sendmail(my_user_name, receiver_email, message)


if __name__ == '__main__':
    return_data = send_email(receiver_email='babaladkaran79@gmail.com', subject='test_sending_email', body= 'Hi There Sending an email from smtplib')
    print('Success Sending an email')
