#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""
import sys
from SimpleEmail import SimpleEmail


def send_email():
    """
    Método que se encarga de iniciar la migración de la información, únicamente recibe un parámetro el
    cual es ingresado mediante la ejecución del script mediante linea de comandos.
    """
    print("PROCESS: Inicia Codigo Python")
    properties_route_file = str(sys.argv[1])    # Direccion del Archivo de propiedades
    mail_account_to = str(sys.argv[2])          # cuenta a la que se va a enviar el correo Electronico
    user_name_report = str(sys.argv[3])         # nombre del Usuario que va a recibir el mensaje
    user_number_report = str(sys.argv[4])       # numero de reporte del Usuario
    user_date_report = str(sys.argv[5])         # fecha de reporte del Usuario
    user_detail_report = str(sys.argv[6])       # detalle de reporte del Usuario
    user_archive_report = str(sys.argv[7])       # archivo de reporte del Usuario
    simple_email = SimpleEmail.SimpleEmail(properties_route_file,
                                           mail_account_to,
                                           user_name_report,
                                           user_number_report,
                                           user_date_report,
                                           user_detail_report,
                                           user_archive_report)
    simple_email.send_simple_email()


"""
Metodo Inicial para Iniciar Todo el Proceso de migrar Puntos.
"""

if __name__ == "__main__":
    send_email()
