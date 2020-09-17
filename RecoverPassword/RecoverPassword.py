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


class RecoverPassword:
    __htmlTemplate = "<p><img style=\"display: block; margin-left: auto; margin-right: " \
                     "auto;\"src=\"https://secretariademovilidad.quito.gob.ec/images/imagenes_movilizateuio" \
                     "/Logo_Secretaria_sin_fondo.png\"  alt=\"logo\" width=\"239\" height=\"83\" /></p>\n <p " \
                     "style=\"text-align: center;\">Estimado <strong><<#username>></strong>&nbsp; , esta es su " \
                     "contrase&ntilde;a para acceder a la aplicaci&oacute;n MovilizateUIO</p>\n <p " \
                     "style=\"text-align:  center;\"><br /><strong><<#password>></strong></p>\n <p>&nbsp;</p>\n " \
                     "<p>Saludos Cordiales <br " \
                     "/>Secretaria de Movilidad <br />Distrito Metropolitano de Quito</p> "

    __htmlTemplateGmail = "<p><img style=\"display: block; margin-left: auto; margin-right: auto;\" " \
                          "src=\"https://secretariademovilidad.quito.gob.ec/images/imagenes_movilizateuio" \
                          "/Logo_Secretaria_sin_fondo.png\" alt=\"logo\" width=\"239\" height=\"83\" /></p>\n <p " \
                          "style=\"text-align: center;\">Estimado <strong><<#username>>,</strong> su registro se " \
                          "realizo mediante el bot&oacute;n de google, usted no posee contrase&ntilde;a por favor " \
                          "ingrese mediante el bot&oacute;n de google.</p>\n <p style=\"text-align: center;\"><br " \
                          "/><strong>password</strong></p>\n <p>&nbsp;</p>\n <p>Saludos Cordiales <br />Secretaria " \
                          "de  Movilidad <br />Distrito Metropolitano de Quito</p> "
    __mail_account_to = ''
    __user_name = ''
    __user_password = ''
    __is_google_user = ''

    # VARIABLES PARA CONFIGURAR EL SERVIDOR SMTP
    __mail_port = ''
    __mail_host_name = ''
    __mail_account_user_mail = ''
    __mail_account_password = ''
    __mail_account_cc = ''

    def __init__(self, file_location, mail_account_to, user_name, user_password, is_google_user):
        self.read_properties(file_location)
        self.__mail_account_to = mail_account_to
        self.__user_name = user_name
        self.__user_password = user_password
        self.__is_google_user = is_google_user
        print('hola mundo')

    def read_properties(self, file_location):
        properties = Properties()
        with open(file_location, 'rb') as config_file:
            properties.load(config_file)
        self.__mail_port = properties.get('mail.smtp.port').data
        self.__mail_host_name = properties.get('mail.host.name').data
        self.__mail_account_user_mail = properties.get('mail.account.from.username').data
        self.__mail_account_password = properties.get('mail.account.from.password').data
        self.__mail_account_cc = properties.get('push.messaging.html.CC').data

    def send_simple_email(self):
        try:
            print("sending .....")
            mail_server = SMTP(self.__mail_host_name, self.__mail_port)
            mail_server.ehlo()
            mail_server.starttls()
            mail_server.login(self.__mail_account_user_mail, self.__mail_account_password)
            mail_server.sendmail(self.__mail_account_user_mail, self.get_toaddrs(), self.get_mime_multipart())
            mail_server.quit()
            print("PROCESS: OK")
        except Exception as inst:
            print("PROCESS:" + str(type(inst)))
            print("PROCESS:" + str(inst.args))
            print("PROCESS:" + str(inst))
            print("PROCESS: ERROR ..... !!!")

    def get_toaddrs(self):
        return [self.__mail_account_to]

    def get_mime_multipart(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "RECUPERAR SU PASSWORD"
        msg['From'] = self.__mail_account_user_mail
        msg['To'] = self.__mail_account_to
        template = MIMEText(self.replace_template_variables(), 'html')
        msg.attach(template)
        return msg.as_string()

    def replace_template_variables(self):
        if self.__is_google_user == '1':
            return self.__htmlTemplateGmail \
                .replace('<<#username>>', self.__user_name)
        else:
            return self.__htmlTemplate \
                .replace('<<#password>>', self.__user_password) \
                .replace('<<#username>>', self.__user_name)
