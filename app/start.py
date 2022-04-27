from app.controllers.ListenQueryController import ListenQueryController
import speech_recognition as sr
import time
from sys import exit
import playsound


class Start():
    def __init__(self, parler) -> None:
        self.recog = sr.Recognizer()
        self.parler = parler
        self.parler.say('Bienvenido.')
        self.parler.runAndWait()
        self.limitphrase = 1
        while True:
            with sr.Microphone() as source:
                self.recog.adjust_for_ambient_noise(source, duration=1)
                audio = self.recog.listen(
                    source, phrase_time_limit=self.limitphrase)
                try:
                    tostart = self.recog.recognize_google(
                        audio, language="es-MX")
                    if "vamos" in tostart:
                        self.execCommand()
                except sr.UnknownValueError:
                    continue
                except sr.RequestError as e:
                    print("Error: {0}".format(e))
            time.sleep(1)
            continue

    def execCommand(self) -> None:
        while True:
            played = playsound.playsound("./assets/sounds/sound_one.wav")
            with sr.Microphone() as source:
                self.recog.adjust_for_ambient_noise(source)
                audio = self.recog.listen(source, timeout=10)
            try:
                query = self.recog.recognize_google(audio, language="es-MX")
                print("Dijiste: {}".format(query))
                if query != '':
                    self.parler.say("Aguarda.")
                    self.parler.runAndWait()
                    listenquerycontroller = ListenQueryController(
                        query, False, self.parler)
                    resultquery = listenquerycontroller.validateQuery()
                    print(resultquery)
                    if resultquery == 'exit':
                        self.parler.say("Se cerrará la aplicación")
                        self.parler.runAndWait()
                        exit()
                    else:
                        self.parler.say(resultquery)
                        self.parler.runAndWait()
                    break
                else:
                    self.parler.say("Por favor dime que deseas")
                    self.parler.runAndWait()
            except sr.UnknownValueError:
                self.parler.say("No logro entender lo que dices")
                self.parler.runAndWait()
            except sr.RequestError as e:
                self.parler.say(
                    "No se pudo conectar con el servidor; {0}".format(e))
                self.parler.runAndWait()
            time.sleep(1)
            continue
