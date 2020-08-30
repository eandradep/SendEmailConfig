#!/usr/bin/python3
import subprocess
import sys

list_files = subprocess.run(["/usr/bin/python3",
                             sys.argv[1]+"/MigrateShapeFile/scriptMigrar.py",
                             sys.argv[2]])






