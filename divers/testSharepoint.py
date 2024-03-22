# Assurez-vous d'avoir installé Office365-REST-Python-Client
# pip install Office365-REST-Python-Client
# ou pour la dernière version directement depuis GitHub:
# pip install git+https://github.com/vgrem/Office365-REST-Python-Client.git

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

# Construction de l'URL SharePoint et des identifiants
# sharepoint_base_url = 'https://mycompany.sharepoint.com/teams/sharepointname/'
sharepoint_base_url = 'https://ciesodecigs2e.sharepoint.com/dri/SitePages/'
#sharepoint_user = 'user@mycompany.com'
#sharepoint_password = 'pwd'
sharepoint_user = 'souleysanogo@gs2e.ci'
sharepoint_password = 'forHAKIM78'

# Pour accéder à un dossier spécifique, décommentez et ajustez la ligne suivante:
# folder_in_sharepoint = '/teams/sharepointname/Shared%20Documents/YourFolderName/'
folder_in_sharepoint = '.'  # '.' pour le répertoire racine

# Authentification à SharePoint
auth = AuthenticationContext(sharepoint_base_url)
auth.acquire_token_for_user(sharepoint_user, sharepoint_password)
ctx = ClientContext(sharepoint_base_url, auth)

# Vérification de la connexion
web = ctx.web
ctx.load(web)
ctx.execute_query()
print('Connecté à SharePoint : ', web.properties['Title'])

'''
# Fonction pour obtenir les détails des fichiers dans un dossier SharePoint
def folder_details(ctx, folder_in_sharepoint):
    folder = ctx.web.get_folder_by_server_relative_url(folder_in_sharepoint)
    files = folder.files
    ctx.load(files)
    ctx.execute_query()
    return [file.properties["Name"] for file in files]

# Obtention et impression des détails des fichiers
file_list = folder_details(ctx, folder_in_sharepoint)
print(file_list)
'''
