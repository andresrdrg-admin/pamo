from app.start import Start

class Main():
    def __init__(self) -> None:
        try:
            Start()
        except KeyboardInterrupt:
            print("\nSe cerró la aplicación")
        except Exception as e:
            print("\nError inesperado: "+ str(e))        

startApp = Main()