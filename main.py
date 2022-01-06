from app.start import Start

class Main():
    def __init__(self) -> None:
        try:
            Start()
        except KeyboardInterrupt:
            print("\n\nClose application")
        except Exception as e:
            print("\n\nError inesperado: "+ str(e))
        

startApp = Main()