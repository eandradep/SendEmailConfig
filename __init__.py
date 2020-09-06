#!/usr/bin/python3
import subprocess
import sys

list_files = subprocess.run(["/usr/bin/python3",
                             sys.argv[1]+"/SendEmailConfig/SendEmail.py",
                             sys.argv[2],   # general properties file
                             sys.argv[3],   # cuenta a la que se va a enviar el correo Electronico
                             sys.argv[4],   # nombre del Usuario que va a recibir el mensaje
                             sys.argv[5],   # numero de reporte del Usuario
                             sys.argv[6],   # fecha de reporte del Usuario
                             sys.argv[7],   # detalle de reporte del Usuario
                             sys.argv[8]])  # archivo de reporte del Usuario






