from obj.parreraclient import *

def main():
    client = PArreraClient("python-client")

    # Connexion au serveur
    if client.connectToServeur("ws://127.0.0.1:12345"):
        # Envoi d'un message
        client.sendMessage("Bonjour serveur !")

        # Réception d'une réponse
        response = client.receiveMessage()
        if response:
            print(f"Réponse reçue : {response}")

        # Déconnexion
        client.disconnect()


# Entrée du programme
if __name__ == "__main__":
    main()
