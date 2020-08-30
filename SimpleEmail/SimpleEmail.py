#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jproperties import Properties


class SimpleEmail:
    __mail_port = ''
    __mail_host_name = ''
    __mail_account_user_mail = ''
    __mail_account_password = ''
    __mail_account_cc = ''
    __mail_account_to = ''
    __mail_template_template = ''

    def __init__(self, file_location, mail_account_to):
        self.read_properties(file_location)
        self.__mail_account_to = mail_account_to

    def read_properties(self, file_location):
        properties = Properties()
        with open(file_location, 'rb') as config_file:
            properties.load(config_file)
        self.__mail_port = properties.get('mail.smtp.port').data
        self.__mail_host_name = properties.get('mail.host.name').data
        self.__mail_account_user_mail = properties.get('mail.account.from.username').data
        self.__mail_account_password = properties.get('mail.account.from.password').data
        self.__mail_account_cc = properties.get('push.messaging.html.CC').data
        self.__mail_template_template = properties.get('push.messaging.html.template').data

    def send_simple_email(self):
        try:
            print("sending .....")
            mail_server = SMTP(self.__mail_host_name, self.__mail_port)
            mail_server.ehlo()
            mail_server.starttls()
            mail_server.login(self.__mail_account_user_mail, self.__mail_account_password)
            mail_server.sendmail(self.__mail_account_user_mail, self.get_toaddrs(), self.get_mime_multipart())
            mail_server.quit()
            print("OK ..... !!!")
        except :
            print("ERROR ..... !!!")

    def get_toaddrs(self):
        return [self.__mail_account_to] + [self.__mail_account_cc]

    def get_mime_multipart(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "NOTIFICACION"
        msg['From'] = self.__mail_account_user_mail
        msg['To'] = self.__mail_account_to
        template = MIMEText(self.__mail_template_template, 'html')
        msg.attach(template)
        return msg.as_string()
