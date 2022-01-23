from app.controllers.ListenQueryController import ListenQueryController
import speech_recognition as sr
import time

class Start():
    def __init__(self) -> None:
        print('Por favor hable al microfono para dar una instrucción')
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language="es-MX")
                print("<--- Tú: {}".format(query))
                if query != '':
                    print("---> Estoy examinando como puedo resolver tu petición...")
                    ListenQueryController(query)
                else:
                    print("---> No entiendo lo que has pedido por favor repite la instrucción")                
            except sr.UnknownValueError:
                print("Google Speech No pudo reconocer el audio")
            except sr.RequestError as e:
                print("No se pudo conectar con el servidor; {0}".format(e))
            print('Aguarde...')
            time.sleep(.2)
            continue