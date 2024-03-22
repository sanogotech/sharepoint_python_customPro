from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
import os
import ssl

# Paramètres de connexion
sharepoint_base_url = "https://ciesodecigs2e.sharepoint.com/dri/"
sharepoint_user = 'souleysanogo@gs2e.ci'
sharepoint_password = 'forHAKIM78'

## folder_in_sharepoint =  '/Documents%20partages/CCDC' # Ajustez ce chemin vers votre dossier

#folder_in_sharepoint =  '/Documents%20partages/CCDC' # Ajustez ce chemin vers votre dossier
folder_in_sharepoint =  '/CCDC'

# Désactiver la vérification de certificat SSL pour toute l'application (FORTEMENT DÉCONSEILLÉ)
ssl._create_default_https_context = ssl._create_unverified_context

# Désactiver la vérification de certificat SSL (FORTEMENT DÉCONSEILLÉ dans les environnements de production)
import requests
requests.packages.urllib3.disable_warnings()
os.environ['PYTHONHTTPSVERIFY'] = '0'

try:
    # Authentification
    auth_ctx = AuthenticationContext(sharepoint_base_url)
    if auth_ctx.acquire_token_for_user(sharepoint_user, sharepoint_password):
        ctx = ClientContext(sharepoint_base_url, auth_ctx)
        web = ctx.web
        ctx.load(web)
        ctx.execute_query()
        print(f"Connecté à SharePoint: {web.properties['Title']}")
        
        '''
        # Accéder au dossier spécifique
        folder = ctx.web.get_folder_by_server_relative_url(folder_in_sharepoint)
        ctx.load(folder)
        ctx.execute_query()
        print(f"Accès au dossier: {folder.server_relative_url}")

        # Lister les fichiers dans le dossier
        files = folder.files
        ctx.load(files)
        ctx.execute_query()
        print("Fichiers dans le dossier:")
        for file in files:
            print(file.properties["Name"])
        '''
        
    else:
        print("Échec de l'authentification.")
except Exception as e:
    #print(f"Une erreur est survenue: {str(e)}")
    import traceback
    print(traceback.format_exc())  # Affiche la pile d'appels complète

