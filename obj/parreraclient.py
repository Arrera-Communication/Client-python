# parreraclient

import asyncio
import websockets


class PArreraClient:
    def __init__(self, uri):
        """
        Initialise le client WebSocket avec une URI (adresse du serveur).
        :param uri: L'adresse WebSocket du serveur (ex: ws://127.0.0.1:12345).
        """
        self.uri = uri
        self.connection = None  # Représente la connexion WebSocket

    async def connect(self):
        """
        Établit une connexion avec le serveur WebSocket.
        """
        try:
            self.connection = await websockets.connect(self.uri)
            print(f"Connecté au serveur : {self.uri}")
        except Exception as e:
            print(f"Erreur lors de la connexion : {e}")
            self.connection = None

    async def send_message(self, message):
        """
        Envoie un message au serveur.
        :param message: Texte à envoyer (str).
        """
        if self.connection:
            try:
                await self.connection.send(message)
                print(f"Message envoyé : {message}")
            except Exception as e:
                print(f"Erreur lors de l'envoi du message : {e}")
        else:
            print("Aucune connexion active pour envoyer des messages.")

    async def receive_message(self):
        """
        Reçoit un message depuis le serveur.
        :return: Texte (str) reçu depuis le serveur.
        """
        if self.connection:
            try:
                response = await self.connection.recv()
                print(f"Message reçu : {response}")
                return response
            except Exception as e:
                print(f"Erreur lors de la réception du message : {e}")
        else:
            print("Aucune connexion active pour recevoir des messages.")
            return None