import sharepy

import os
import ssl

# Remplacez ces valeurs par vos propres informations
username = "souleysanogo@gs2e.ci"
password = "forHAKIM78"
#site_url = "https://votredomaine.sharepoint.com/sites/votre_site"
site_url = "https://ciesodecigs2e.sharepoint.com/dri"
#folder_path = "/sites/votre_site/Shared Documents/Chemin/vers/le/dossier"
folder_path = "/sites/dri/Documents%20partages/CCDC"


# Désactiver la vérification de certificat SSL pour toute l'application (FORTEMENT DÉCONSEILLÉ)
ssl._create_default_https_context = ssl._create_unverified_context

# Désactiver la vérification de certificat SSL (FORTEMENT DÉCONSEILLÉ dans les environnements de production)
import requests
requests.packages.urllib3.disable_warnings()
os.environ['PYTHONHTTPSVERIFY'] = '0'

# Créer une session SharePy
s = sharepy.connect(site_url, username, password)

# Construire l'URL de l'API pour accéder au dossier spécifié
api_url = f"{site_url}/_api/web/GetFolderByServerRelativeUrl('{folder_path}')/Files"

# Effectuer une requête GET pour obtenir la liste des fichiers
r = s.get(api_url)
if r.status_code == 200:
    files = r.json()

    # Parcourir et afficher les noms des fichiers
    for file in files.get('d').get('results', []):
        print(file['Name'])
else:
    print(f"Erreur: {r.status_code}")
