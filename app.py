import requests

def get_random_joke():
    # Endpoint de l'API pour récupérer une blague aléatoire en français
    url = 'https://api.chucknorris.io/jokes/random?language=fr'
    
    try:
        # Effectuer une requête GET à l'API
        response = requests.get(url)
        
        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            # Extraire les données JSON de la réponse
            data = response.json()
            
            # Récupérer la blague depuis les données
            joke = data['value']
            
            return joke
        else:
            # Afficher un message d'erreur si la requête a échoué
            print(f"Erreur lors de la requête : {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Afficher une erreur en cas de problème de connexion
        print(f"Erreur de connexion : {e}")

# Appel de la fonction pour obtenir une blague aléatoire en français
random_joke = get_random_joke()
print(random_joke)
