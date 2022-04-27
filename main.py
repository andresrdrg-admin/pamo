from app.start import Start
import pyttsx3

class Main():
    def __init__(self) -> None:
        parler = pyttsx3.init()
        voices = parler.getProperty('voices')       #getting details of current voice
        parler.setProperty("rate", 150)
        parler.setProperty("volume", 100)
        parler.setProperty('voice', voices[0].id)
        try:
            Start(parler)
        except KeyboardInterrupt:
            parler.say("Se cerrará la aplicación.")
            parler.runAndWait()
        except Exception as e:
            parler.say("Hubo un error inesperado")        
            print("Hubo un error inesperado: "+ str(e))        
            parler.runAndWait()
startApp = Main()