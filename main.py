import subprocess
import sys
import os

def limpiar_consola():
    # Función para limpiar la consola según el sistema operativo
    if sys.platform.startswith('win'):
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Unix/Linux/Mac

def mostrar_divisor(simb="="):
    print(simb * 30)

def mostrar_menu():
    mostrar_divisor()
    print("Menú:")
    mostrar_divisor()
    print("1. Guardar el certificado de proxy en el dispositivo.")
    print("2. Correr objection.")
    print("3. Instalar apk original.")
    print("4. Instalar apk modificada con objection.")
    print("0. Salir del programa.")
    mostrar_divisor()
    
    
#=======================EJECUTADOR DE CMD==========================#   
def cmd(comando, rta=False):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    if (rta):
        return resultado
    
    
#=========================PUNTO NUMERO 1===========================#
#Verificamos la existencia de dispositivos conectados.
def verificar_dispositivos_conectados():
    try:
        resultado = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
        lista_dispositivos = resultado.stdout.splitlines()
        
        # Si se encontraron dispositivos
        if len(lista_dispositivos) > 2:
            print("Dispositivo Android conectado")
            return True
        else:
            print("No se encontraron dispositivos Android conectados.")
            return False
    
    except subprocess.CalledProcessError as e:
        print("Ocurrió un error al ejecutar ADB:", e)
        return False

 #=========================PUNTO NUMERO 2===========================#   
def correr_objection(dirapk):
    limpiar_consola()
    mostrar_divisor()
    print("Corriendo objection...")
    mostrar_divisor()

    try:
        # Ejecutar objection con el comando específico
        # Comando completo a ejecutar en una consola Windows
        comando ='objection patchapk -s' + dirapk + ' -N -d -2'

        # Ejecutar los comandos en la consola de Windows
        proceso = subprocess.Popen(comando, shell=True)
        proceso.wait()
        input("\nPresiona Enter para volver al menú...")
        
    
    except Exception as e:
        print("Ocurrió un error al ejecutar objection:", e)
        input("\nPresiona Enter para volver al menú...")   

def modifdirapk(dirorig):
    
    nombre_archivo, extension = os.path.splitext(dirorig)

    # Agregar ".objection" justo antes de la extensión
    nueva_ruta_archivo = f"{nombre_archivo}.objection{extension}"
    return dirorig

    
 #=========================PUNTO NUMERO 3===========================#    
def instalar_apk(ruta_apk):
    try:
        # Reemplaza 'ruta_del_archivo.apk' con la ruta completa de tu APK original
        subprocess.run(['adb', 'install', ruta_apk], check=True)
        print("Aplicación fue instalada exitosamente.")
    
    except subprocess.CalledProcessError as e:
        print("Ocurrió un error al instalar la APK:", e)   
    
    
    
    
    
    
def main():
    global ubiApkOrig
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar (0 para salir): ")

        if opcion == "1":
            limpiar_consola()
            
            if(verificar_dispositivos_conectados()):
                mostrar_divisor("-")
                print("Vamos a guardar el certificado proxy en el dispositivo!")
                print("Para que el proceso de guardado funcione correctamente es necesario que:")
                print("1. Tener instalado ADB")
                print("2. Haber generado ya el certificado y tener a mano la ubicación del mismo.")
                mostrar_divisor(".")
                ubiCertif = input("Porfavor ingrese la ruta del archivo '.cer': ")
                
                #Pusheamos el certificado:
                comando = "adb push "+ ubiCertif +" /sdcard/Download/cacert.cer"
                cmd(comando)
                print("Certificado ingresado con exito!")
                print("Lo encontrará en /sdcard/Download")
                
            else:
                print("No se encontro ningún dispositivo. Es necesario tener conectado uno para realizar el proceso")
            
            # Aquí colocarías el código para ejecutar la opción 1
            
        elif opcion == "2":
            mostrar_divisor("-")
            dirapk = input("Ingrese la dirección de la apk que quiere modificar: ")
            correr_objection(dirapk)
            
        elif opcion == "3":
            mostrar_divisor("-")
            ubiApkOrig = input("Porfavor inserte la ubicación de la apk que quiere instalar: ")
            instalar_apk(ubiApkOrig)
            
        elif opcion == "4":
            mostrar_divisor("-")
            dirapkmod = input("Ingrese la direccion de la apk modificada: ")
            instalar_apk(dirapkmod)            
        elif opcion == "0":
            print("Saliendo del programa...")
            sys.exit()

        else:
            print("Opción no válida. Por favor, ingrese un número válido de opción.")

if __name__ == "__main__":
    main()
