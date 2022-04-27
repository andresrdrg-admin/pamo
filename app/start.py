from app.controllers.ListenQueryController import ListenQueryController
import speech_recognition as sr
import time

class Start():
    def __init__(self, parler) -> None:
        self.parler = parler      
        self.parler.say('Hola, soy Pámo, tu asistente personal. Me has activado.')
        self.parler.runAndWait()

        print("Ejecutando...")
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                tostart = r.recognize_google(audio, language="es-MX")
                print("Dijiste: {}".format(tostart))
                if "vamos" in tostart:
                    self.execCommand()
            except sr.UnknownValueError:
                parler.say("No logro entender lo que dices")
                parler.runAndWait()
            except sr.RequestError as e:
                parler.say("No se pudo conectar con el servidor; {0}".format(e))
                parler.runAndWait()
            time.sleep(.2)
            continue



    def execCommand(self) -> None:
        self.parler.say("¿En que te puedo colaborar?")
        self.parler.runAndWait()
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                tostart = r.recognize_google(audio, language="es-MX")
                print("Dijiste: {}".format(tostart))
                query = r.recognize_google(audio, language="es-MX")
                if query != '':
                    self.parler.say("Estoy examinando como puedo resolver tu petición. Aguarda...")
                    self.parler.runAndWait()
                    listenquerycontroller = ListenQueryController(query, False, self.parler)
                    resultquery = listenquerycontroller.validateQuery()
                    print(resultquery)
                    self.parler.say(resultquery)
                    self.parler.runAndWait()
                else:
                    self.parler.say("Por favor dime que deseas")                
                    self.parler.runAndWait()
            except sr.UnknownValueError:
                self.parler.say("No logro entender lo que dices")
                self.parler.runAndWait()
            except sr.RequestError as e:
                self.parler.say("No se pudo conectar con el servidor; {0}".format(e))
                self.parler.runAndWait()
            time.sleep(.2)
            continue