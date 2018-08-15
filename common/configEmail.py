import smtplib,readConfig
from email.mime.text import MIMEText

#发件人信息和收件人信息
config=readConfig.Readconfig()
class email:
    def __init__(self):
        pass


    def sendEmail(self,neirong):
        email_host = config.get_email('email_host')
        email_user = config.get_email("email_user")
        email_pass = config.get_email("email_pass")
        sener = config.get_email("sener")
        receiver = config.get_email("receiver")
        subject = config.get_email("subject")
        msg=MIMEText(neirong,'html','utf-8')
        msg['Subject']=subject
        msg['From']=sener
        msg['To']=receiver
        try:
            smtp=smtplib.SMTP()
            smtp.connect(email_host,25)
            smtp.login(email_user,email_pass)
            smtp.sendmail(sener,receiver,msg.as_string())
            print("邮件发送成功！")
        except smtplib.SMTPException:
            print("Error:邮件发送失败！")
