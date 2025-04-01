from obj.parreraclient import *

async def main():
    # Adresse WebSocket du serveur Qt
    server_uri = "ws://127.0.0.1:12345"

    # Créer un client WebSocket
    client = PArreraClient(server_uri)

    # Connexion au serveur
    await client.connect()

    # Envoyer un message
    await client.send_message("Bonjour depuis le client Python!")

    # Recevoir une réponse
    await client.receive_message()

    # Fermer la connexion
    # await client.close()


# Entrée du programme
if __name__ == "__main__":
    asyncio.run(main())
