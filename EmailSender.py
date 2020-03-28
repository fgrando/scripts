#!/usr/bin/python

import logging
import smtplib
import mimetypes
import os
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from email import encoders


class EmailSender():
    """Simple client to send emails.

    Args:
        smtp_host (str): SMTP host ('smtp.gmail.com').
        smtp_port (int): SMTP host port (465).
        username (str): Client email ('yoremail@gmail.com'). This is also the sender.
        password (str): Your password ('Password123')
        log (logging, optional): Logging facility see logs (logging.getLogger()).

    """


    def __init__(self, smtp_host, smtp_port, username, password, log=None):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

        if log != None:
            self.log = log
        else:
            self.log = logging.getLogger()

    def send(self, recipients, subject, body, attachments = []):
        """Send an email. Login is done with SMTP SSL.

        Args:
            recipients (list): List of emails to receive this message.
            subject (str): The email subject.
            body (str): The email text (body).
            atttachments (list, optional): List of files to be attached.

        Returns:
            True if successful, otherwise False.
        """
        result = True

        try:
            self.log.debug('creating client [{}] [{}] [{}]'.format(self.smtp_host, self.smtp_port, self.username))
            server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
            server.login(self.username, self.password)
        except:
            self.log.error("Login failed!")
            return False

        self.log.debug('building email from [{}] called [{}]'.format(self.username, subject))
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.username

        self.log.debug('attaching body [{}]'.format(body))
        txt = MIMEText(body)
        msg.attach(txt)

        try:
            self.log.debug('loading attachments...')
            for path in attachments:
                self.log.debug('attaching [{}]'.format(path))
                self.load_attachment(path, msg)
        except:
            self.log.error("Failed to load attachments")
            return False

        mail_ascii = msg.as_string() #.encode('ascii', 'ignore').decode('ascii')

        self.log.debug('sending email...')
        for dst in recipients:
            sent = False # flag to control the result
            msg['To'] = dst
            try:
                server.sendmail(self.username, dst, mail_ascii)
                sent = True
            except:
                pass

            if not sent:
                self.log.error('sending failed to [{}]'.format(dst))
            else:
                self.log.debug('sending to [{}]'.format(dst))

            resutl = result and sent #increment global result

        server.quit()
        if result:
            self.log.debug('finished')
        else:
            self.log.warning('finished with errors')

        return result


    def load_attachment(self, filepath, message):
        """Load files as attachments. If the file is not text,
        image or audio, it will be loaded with MIMEBase and encoded.

        Args:
            filepath (str): The file path.
            message (MIMEMultipart): The email to attach the file.
        """

        msg = None
        content_type, encoding = mimetypes.guess_type(filepath)

        if (content_type is None) or (encoding is not None):
            content_type = 'application/octet-stream'

        main_type, sub_type = content_type.split('/', 1)

        self.log.debug("{}: content [{}] encoding [{}] type [{}] sub [{}]".format(\
            filepath, content_type, encoding, main_type, sub_type))

        if main_type == 'text':
            fp = open(filepath, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()

        elif main_type == 'image':
            fp = open(filepath, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()

        elif main_type == 'audio':
            fp = open(filepath, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()

        else:
            fp = open(filepath, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            fp.close()

        filename = os.path.basename(filepath)
        self.log.debug('attachment filename [{}]'.format(filename))

        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)


# Example
if __name__ == '__main__':
    # Create a log so we can see get some output (not mandatory, but wise)
    log = logging.getLogger("sender")
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('%(name)s-%(levelname)s: %(message)s'))
    log.addHandler(ch)

    # inform the user credentials
    sender = EmailSender("smtp.gmail.com", 465, "<youremail>@gmail.com", "<yourpassword>", log)

    log.info("Sending simple email")
    # simple email
    ret = sender.send(["<destination>@gmail.com"], "simple email", "hello world")

    log.info("Sending email with attachments")
    # email with attachments
    ret = sender.send(\
        [\
            "<destination>@gmail.com"\
        ],\
        "This email contains attachments",\
        "Lorem ipsum lalalala",\
        [\
            "/home/fgrando/fix_mouse.sh",\
            "/home/fgrando/Pictures/mypic.png",\
            "/home/fgrando/Desktop/file.pdf",\
            "/home/fgrando/Desktop/audio.mp3",\
            "/home/fgrando/Desktop/video.mp4",\
            "/home/fgrando/Desktop/zipped.zip"\
        ]\
    )


