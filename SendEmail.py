#!/usr/bin/python3
"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    @author Edison Andrade
    @email eandradep@est.ups.edu.ec
"""
import sys
from SimpleEmail import SimpleEmail


def iniciar_migracion():
    """
    Método que se encarga de iniciar la migración de la información, únicamente recibe un parámetro el
    cual es ingresado mediante la ejecución del script mediante linea de comandos.
    """
    print("PROCESS: Inicia Codigo Python")
    properties_route_file = str(sys.argv[1])
    mail_account_to = str(sys.argv[2])
    user_name_report = str(sys.argv[3])
    user_number_report = str(sys.argv[3])
    simple_email = SimpleEmail.SimpleEmail(properties_route_file, mail_account_to, user_name_report, user_number_report)
    simple_email.send_simple_email()


"""
Metodo Inicial para Iniciar Todo el Proceso de migrar Puntos.
"""

if __name__ == "__main__":
    iniciar_migracion()
