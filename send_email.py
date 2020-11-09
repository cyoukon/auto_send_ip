#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import config
from log import write_log


class SendEmail():
    """发送邮件"""

    def __init__(self, text):
        self.text = text
        self.message = MIMEText(text, 'plain', 'utf-8')
        self.message['From'] = formataddr(["IP地址变化", config.smtp_user])
        self.message['To'] = config.send_to              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        self.message['Subject'] = 'ip'                # 邮件的主题，也可以说是标题

    def send(self):
        try:
            smtpObj = smtplib.SMTP(config.smtp_server, config.smtp_port)
            smtpObj.ehlo()
            smtpObj.login(config.smtp_user, config.smtp_pwd)
            smtpObj.sendmail(config.smtp_user, config.send_to, self.message.as_string())
            write_log("邮件发送成功")
            smtpObj.quit()  # 关闭连接
        except smtplib.SMTPException:
            write_log("Error: 无法发送邮件")
