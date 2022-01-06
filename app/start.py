from app.controllers.ListenQueryController import ListenQueryController
class Start():
    def __init__(self) -> None:
        print('¡Hola! Soy POLA tu asistente personal personalizada')
        while True:
            query = input("Tú: ")
            if query != '':
                print("Estoy examinando como puedo resolver tu petición...")
                ListenQueryController(query)
            else:
                print("Por favor escribe una petición que pueda entender")