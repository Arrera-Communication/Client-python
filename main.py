from obj.parreraclient import *

async def main():
    # Adresse WebSocket du serveur Qt
    server_uri = "ws://127.0.0.1:12345"

    # Créer un client WebSocket
    client = PArreraClient()

    # Connexion au serveur
    await client.connectToServeur(server_uri)

    # Envoyer un message
    await client.sendMessage("Bonjour depuis le client Python!")

    # Recevoir une réponse
    await client.receiveMessage()

    # Fermer la connexion
    # await client.close()


# Entrée du programme
if __name__ == "__main__":
    asyncio.run(main())
