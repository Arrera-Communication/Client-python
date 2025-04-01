# parreraclient

import asyncio
import websockets


class PArreraClient:
    def __init__(self):
        self.__uri = None
        self.__connection = None  # Représente la connexion WebSocket

    async def connectToServeur(self, uri:str):
        if (uri == ""):
            return False
        else :
            self.__uri = uri
            try:
                self.__connection = await websockets.connect(self.__uri)
                return True
            except Exception as e:
                self.__connection = None
                return False


    async def send_message(self, message):
        if self.__connection:
            try:
                await self.__connection.send(message)
                return True
            except Exception as e:
                return False
        else:
           return False

    async def receive_message(self):
        if self.__connection:
            try:
                response = await self.__connection.recv()
                return response
            except Exception as e:
                return None
        else:
            return None