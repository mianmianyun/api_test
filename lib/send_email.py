import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from api_test.config.config import *

def send_mail():
    msg=MIMEText('eee','plain','utf-8')

    #定义邮件内容
    # msg=MIMEMultipart('mixed')
    #
    #定义邮件html内容
    # html_text=open(report_file,encoding='utf-8').read()
    # msg_html_text=MIMEText(html_text,'html','utf-8')
    # msg.attach(msg_html_text)
    #
    # #定义邮件附件
    # sendfile=open(report_file,'rb').read()
    # msg_text_att=MIMEText(sendfile,'base64','utf-8')
    # msg_text_att["Content-Type"] = 'application/octet-stream'
    # msg_text_att['Content-Disposition']='attachment; filename="report.html"'
    # msg.attach(msg_text_att)

    msg['From'] = sender  # 发件人
    msg['To'] = reciever # 收件人
    msg['Subject'] = suject  # 邮件主题

    #连接邮箱服务器，发送邮件
    try:
        smtp=smtplib.SMTP_SSL(smtp_sever) #连接邮箱服务器
        smtp.login(sender, password)  # 用户名和密码登录
        smtp.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息。
        smtp.sendmail(sender,reciever, msg.as_string()) #发送邮件
        logging.info("邮件发送完成")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

if __name__=='__main__':
    send_mail()

