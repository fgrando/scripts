import smtplib

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
    sent = send_gmail("senhoriluminati@gmail.com", # your gmail
               "mascadagloriosa",           # your gmail password
               "fernandozatt@gmail.com",    # recipient
               "JARVIS",                    # subject
               "POWER FINE"                 # body
               )
    if sent:
        exit(0)

    else:
        print("not sent")
        exit(-1)
