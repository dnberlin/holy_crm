import logging
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 
# Import the email modules we'll need
from email.parser import BytesParser, Parser
from email.policy import default

import time

class EmailHandler:

    __log__ = logging.getLogger('holy-crm')

    def __init__(self, config):
        self.smtp_server = config.get('mail', dict()).get('smtp_server')
        self.smtp_port = config.get('mail', dict()).get('smtp_port')
        self.user_email = config.get('mail', dict()).get('user_email')
        self.user_pw = config.get('mail', dict()).get('user_pw')
        self.sender_name = config.get('mail', dict()).get('sender_name')
        pass

    def send_email(self, data, attachment_path=None):
        self.__log__.info("Sending email...")
        print(F"Recipient name: {data['recipient_name']}")
        print(f"Recipient address: {data['recipient_email']}")
        print(f"Subject: {data['subject']}")
        print(f"Body: {data['body']}")

        msg = MIMEMultipart()
        msg['Subject'] = data['subject']
        msg['From'] = self.sender_name + ' <' + self.user_email + '>' 
        msg['To'] = data['recipient_name'] + ' <' + data['recipient_email'] + '>'
        message = data['body']
        msg.attach(MIMEText(message))

        # Attach file
        if attachment_path != None:
            print('Attachment mode activated:')
            msg = self.__attach_file(msg, attachment_path)

        mailserver = self.__establish_connection()

        mailserver.sendmail(self.user_email, data['recipient_email'], msg.as_string())
        print("Sleep 5 seconds.")
        time.sleep(5)
        
        mailserver.quit()

    def __attach_file(self, msg, attachment_path):
        # open the file to be sent  
        filename = attachment_path.split('/')[-1]
        # Filename modifications
        #filename_modified = 'Felix_Werner_Mietervorstellung.pdf'
        filename_modified = filename.split('gen_')[-1]
        print(f" Attaching file: {filename}. Source: {attachment_path} \n")
        attachment = open(attachment_path, "rb") 
  
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 
          
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
          
        # encode into base64 
        encoders.encode_base64(p) 
           
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename_modified) 
          
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 
        
        return msg

    def __establish_connection(self):
        mailserver = smtplib.SMTP(self.smtp_server ,self.smtp_port)
        mailserver.set_debuglevel(1)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login(self.user_email, self.user_pw)

        return mailserver