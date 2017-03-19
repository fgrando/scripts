import smtplib

from mysettings import * # to get my email account and passwords

#thanks to: http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python

def send_gmail(user, passwd, recipient, subject, body):
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        # use SSL to avoid problems
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()
        server_ssl.login(user, passwd)  
        server_ssl.sendmail(FROM, TO, message)
        server_ssl.close()
        return True
    
    except:
        return False

if __name__ == "__main__":
    # replace my_send_gmail_* with your settings
    sent = send_gmail(my_send_gmail_user,   # your gmail
               my_send_gmail_pass,          # your gmail password
               my_send_gmail_dest,          # recipient
               my_send_gmail_subj,          # subject
               my_send_gmail_text           # body
               )
    if sent:
        exit(0)

    else:
        print("not sent")
        exit(-1)
