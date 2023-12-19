import subprocess

# Comando que quieres ejecutar en la consola de Windows
comando = "dir"  # Puedes cambiar esto por el comando que desees ejecutar

# Ejecutar el comando en la consola de Windows
resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

# Mostrar el resultado
#print(resultado.stdout)

import os

ruta_archivo = r"C:\apktool\app-release.apk"

# Separar la ruta del archivo en nombre y extensión
nombre_archivo, extension = os.path.splitext(ruta_archivo)

# Agregar ".objection" justo antes de la extensión
nueva_ruta_archivo = f"{nombre_archivo}.objection{extension}"

print(nueva_ruta_archivo)
