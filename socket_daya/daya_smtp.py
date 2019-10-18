import smtplib
from email.mime.text  import MIMEText
from email.header import Header
import os

sender = "2830116055@qq.com"
# 发送者
receiver = ['2830116055@qq.com',"513077914@qq.com","978058532@qq.com"]
# 接受者
mail_host = "smtp.qq.com"
# 发送的服务器
mail_port = 465
# 服务器的端口
mail_user = '2830116055'
# 邮箱的登陆者
mail_pass = 'gcilsdhclkfmdead'
# 邮箱的验证码--不是自己密码

def daya_email(title):
    #发送的主程序
    msg = MIMEText(open("test.py","rb").read(),"plain","utf-8")
    # 设置我的邮件的值的类型和格式
    msg['From']=Header(sender)
    # 写发送者
    msg['To'] = Header(str(":".join(receiver)))
    # 写接受者
    msg['Subject'] = Header(title)

    #形成的就是一个文件Header--html
    #文件  “你好” "plain","utf-8"     From -sender   To-receiver   title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,mail_port)
        # 登录发件服务器
        smtpObj.login(mail_user,mail_pass)
        # 使用你的账户和密码登录
        smtpObj.sendmail(sender,receiver,msg.as_string())
        #设置发送邮件者和接受者，发送的信息
        smtpObj.quit()
        #完成就退出
        return "success"
    except smtplib.SMTPException as e:
        return e

if __name__ == '__main__':
    send = daya_email("达亚测试")
    print(send)