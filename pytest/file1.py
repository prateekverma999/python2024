import file3

class weather:
    def __init__(self,app) -> str:
        self.app=app
    
    def aws(self):
        app = self.app
        goApp = file3.goApp
        flaskApp = file3.flaskApp
        javaApp = file3.javaApp
        if app=="goApp":
            url=f"{file3.url}:{goApp}"
        elif app=="flaskApp":
            url=f"{file3.url}:{flaskApp}"
        elif app=="javaApp":
            url=f"{file3.url}:{javaApp}"
        else:
            url="wrong"
        return url
    
    def userIn():
        x = 0
        while True:
            app = weather(input("Enter app name : "))
            url = app.aws()
            if url=="wrong":
                print("Wrong server!!")
                x += 1
                print(f"your attempt count: {x}, remaining attempt: {3-x}")
                if x == 3:
                    break
            else:
                print(url)
                break

