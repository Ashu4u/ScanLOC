#!/usr/bin/env python3

import smtplib
# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================
def my_function(value,body):
        gmail_user = 'patel.ashish874@gmail.com'
        gmail_app_password = 'cuevjlvqcspgaysh'
        sent_from = gmail_user
        sent_to = [value]
        sent_subject = "Scan Results"
        sent_body =("Hey, what's up? friend!\n"
             "Hello, \nI hope you have been well!"
             +body+
             "Cheers,\n"
             "Ashish\n")

        email_text = """\
         From: %s
         To: %s
         Subject: %s
         %s
         """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_app_password)
            server.sendmail(sent_from, sent_to, email_text)
            server.close()

            print('Email sent!')
        except Exception as exception:
            print("Error: %s!\n\n" % exception)