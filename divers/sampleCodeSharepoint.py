from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext
import os
import ssl

#site_url = "https://XXX.sharepoint.com/sites/mysite"
site_url = "https://ciesodecigs2e.sharepoint.com/dri/"
#client_id = "your-client-id"
#client_secret = "your-client-secret"

client_id = "souleysanogo"
client_secret = "forHAKIM78"

# Désactiver la vérification de certificat SSL pour toute l'application (FORTEMENT DÉCONSEILLÉ)
ssl._create_default_https_context = ssl._create_unverified_context

# Désactiver la vérification de certificat SSL (FORTEMENT DÉCONSEILLÉ dans les environnements de production)
import requests
requests.packages.urllib3.disable_warnings()
os.environ['PYTHONHTTPSVERIFY'] = '0'

# Configurer les credentials
credentials = ClientCredential(client_id, client_secret)
ctx = ClientContext(site_url).with_credentials(credentials)

# Essayez d'effectuer une opération pour tester la connexion
web = ctx.web
ctx.load(web)
ctx.execute_query()
print(web.properties['Title'])

'''
# Obtenir l'URL relative du site (SPWeb.ServerRelativeUrl)
web = ctx.web
ctx.load(web)
ctx.execute_query()
server_relative_url = web.server_relative_url

# Construire l'URL relative pour accéder au dossier spécifique
# Remplacez les espaces par %20 ou utilisez urllib.parse.quote pour encoder l'URL.
#folder_url = f"{server_relative_url}/Shared Documents/CCDC".replace(" ", "%20")
folder_url = f"{server_relative_url}/Documents partages/CCDC".replace(" ", "%20")

# Utiliser l'URL construite pour accéder au dossier
folder = ctx.web.get_folder_by_server_relative_url(folder_url)
ctx.load(folder)
ctx.execute_query()

# Afficher le nom du dossier pour confirmer le succès
print(f"Nom du dossier: {folder.properties['Name']}")
'''
