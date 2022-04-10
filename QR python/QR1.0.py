import qrcode
from PIL import Image

from time import sleep, time
from colorama import Cursor, init, Fore

import sys,time
time.sleep(0.2)
init()
print(Fore.MAGENTA +"▒█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░░ 　 ▒█▀▀█ ▒█▀▀█ ")
print("▒█░▄▄ █▀▀ █░░█ █▀▀ █▄▄▀ █▄▄█ █░░█ █░░█ █▄▄▀ 　 ▀▀ 　 ▒█░▒█ ▒█▄▄▀ ")
print("▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ░░ 　 ░▀▀█▄ ▒█░▒█"+ Fore.RESET)
print("")
print("\033[;36m"+"███"+'\033[0;m'"\033[4;35"+"████"+'\033[0;m'"\033[;36m"+"███"+'\033[0;m' "\x1b[1;32m"+"ㅤㅤㅤㅤ+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+""\x1b[1;31m"+"ㅤㅤㅤㅤ[v 1.0]ㅤㅤㅤㅤ"+'\x1b[0;m')
print("\033[1;33m"+"Follow on Github :] https://github.com/ZIX-6 ♥️"+'\033[0;m')
name = Fore.BLACK+"By.ZIX"+Fore.RESET
for L in name:
    sys.stdout.flush()
    print(L,end="")
    time.sleep(0.2)

print("")
time.sleep(0.3)
url = input("\x1b[1;31m"+"Introduzca una URL para el codigo QR: "+'\x1b[0;m')
imagen = qrcode.make(url)

time.sleep(0.3)
nombre = input(Fore.CYAN + "Introduzca el nombre de la imagen: "+Fore.RESET) + '.png'
print("Copiando archivos... ")
for arch in ["111", "222", "333", "444", "555"]:
    sleep(1)
    print(Cursor.UP(1)+Cursor.FORWARD(20)+Fore.GREEN+str(arch))
       
print(">>> Proceso finalizado")
archivo = open(nombre, 'wb')
imagen.save(archivo)
archivo.close()

ruta_de_imagen = './' + nombre
Image.open(ruta_de_imagen).show()
