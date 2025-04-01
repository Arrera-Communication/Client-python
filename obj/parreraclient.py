import websockets


class PArreraClient:
    def __init__(self):
        self.__uri = None
        self.__connection = None  # Représente la connexion WebSocket

    def connectToServeur(self, uri:str):
        if (uri == ""):
            return False
        else :
            self.__uri = uri
            try:
                self.__connection = websockets.connect(self.__uri)
                return True
            except Exception as e:
                self.__connection = None
                return False


    def sendMessage(self, message):
        if self.__connection:
            try:
                self.__connection.send(message)
                return True
            except Exception as e:
                return False
        else:
           return False

    def receiveMessage(self):
        if self.__connection:
            try:
                response = self.__connection.recv()
                return response
            except Exception as e:
                return None
        else:
            return None