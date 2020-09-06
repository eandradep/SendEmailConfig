#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""
from email.mime.application import MIMEApplication
from smtplib import SMTP
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jproperties import Properties


class SimpleEmail:
    # VARIABLES PARA CONFIGURAR EL SERVIDOR SMTP
    __mail_port = ''
    __mail_host_name = ''
    __mail_account_user_mail = ''
    __mail_account_password = ''
    __mail_account_cc = ''
    # VARIABLES PARA ENVIAR EL MENSAJE.
    __mail_account_to = ''
    __mail_template_template = ''
    __user_name_report = ''
    __user_number_report = ''
    __user_date_report = ''
    __user_detail_report = ''
    __user_archive_report = ''

    def __init__(self, file_location, mail_account_to, user_name_report,
                 user_number_report, user_date_report,
                 user_detail_report, user_archive_report):
        self.read_properties(file_location)
        self.__mail_account_to = mail_account_to
        self.__user_name_report = user_name_report
        self.__user_number_report = user_number_report
        self.__user_date_report = user_date_report
        self.__user_detail_report = user_detail_report
        self.__user_archive_report = user_archive_report

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
            print("PROCESS: OK ..... !!!")
        except Exception as inst:
            print("PROCESS:"+str(type(inst)))
            print("PROCESS:"+str(inst.args))
            print("PROCESS:"+str(inst))
            print("PROCESS: ERROR ..... !!!")

    def get_toaddrs(self):
        return [self.__mail_account_to] + [self.__mail_account_cc]

    def get_mime_multipart(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "PROCESO DENUNCIA"
        msg['From'] = self.__mail_account_user_mail
        msg['To'] = self.__mail_account_to
        template = MIMEText(self.replace_template_variables(), 'html')
        msg.attach(template)
        if self.__user_archive_report != 'null':
            with open(self.__user_archive_report, "rb") as f:
                attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header('Content-Disposition', 'attachment',
                              filename=str('REPORT CODE: '+self.__user_number_report))
            msg.attach(attach)
        return msg.as_string()

    def replace_template_variables(self):
        return self.__mail_template_template \
            .replace('<<#NombrePersona>>', self.__user_name_report) \
            .replace('<<#NumeroDenuncia>>', self.__user_number_report) \
            .replace('<<#FechaEnvio>>', self.__user_date_report) \
            .replace('<<#detalleProceso>> ', self.__user_detail_report) \
            .replace('<<#FechaActual>>', time.strftime("%d/%m/%y")+' '+time.strftime("%H:%M:%S"))
