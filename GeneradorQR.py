import qrcode           #importo la librería qrcode para generar códigos QR
from PIL import Image  #importo la librería PIL para manejar imágenes
def generar_codigo_qr():
    url = input("Ingresa el enlace a que querés convertir en QR: ") #pido al usuario el enlace

    qr = qrcode.QRCode(                  #configuración del QR
        version=1,                       #tamaño del QR (1 es el más chico, luego vartía hasta 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  #nivel de corrección de errores (H es el más alto)
        box_size=10,                      #tamaño de cada cuadridito del QR
        border=4                          #tamaño del borde blanco (mínimo es 4)
    )
    qr.add_data(url)                      #agrego el enlace al QR
    qr.make(fit=True)                     #genero el QR

#genero la imagen del QR
    img = qr.make_image(fill_color="black", back_color="white")

#guardar con el nombre dado por el usuario
    nombre_archivo = input("Ingresa el nombre del archivo para guardar el QR: ")
    img.save(f"{nombre_archivo}.png")
    print(f"Código QR guardado como {nombre_archivo}.png")

    img.show()                             #muestro la imagen del QR si se puede


generar_codigo_qr() #llamo a la función para generar el código QR