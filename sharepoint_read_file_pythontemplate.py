#pip install Office365-REST-Python-Client

# courtesy: https://stackoverflow.com/questions/59979467/accessing-microsoft-sharepoint-files-and-data-using-python
# bugs :  https://learn.microsoft.com/en-us/answers/questions/203179/getfolderbyserverrelativeurl-rest-api-return-serve

#Importing required libraries

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File 

import os
import ssl

#Constrtucting SharePoint URL and credentials 
# sharepoint_base_url = 'https://mycompany.sharepoint.com/teams/sharepointname/' ou https://mycompany.sharepoint.com/Sitesharepointname/'
sharepoint_base_url = 'https://mycompany.sharepoint.com/teams/sharepointname/'
sharepoint_user = 'user'
sharepoint_password = 'pwd'
folder_in_sharepoint = ="/sites/sub_site/Shared%20Documents/YourFolderName/"


#Constructing Details For Authenticating SharePoint

# Emplacement local pour télécharger les fichiers
download_path = './downloads/'

# Désactiver la vérification de certificat SSL pour toute l'application (FORTEMENT DÉCONSEILLÉ)
ssl._create_default_https_context = ssl._create_unverified_context

# Désactiver la vérification de certificat SSL (FORTEMENT DÉCONSEILLÉ dans les environnements de production)
import requests
requests.packages.urllib3.disable_warnings()
os.environ['PYTHONHTTPSVERIFY'] = '0'

auth = AuthenticationContext(sharepoint_base_url)

auth.acquire_token_for_user(sharepoint_user, sharepoint_password)
ctx = ClientContext(sharepoint_base_url, auth)
web = ctx.web
ctx.load(web)
ctx.execute_query()

# Affichage des informations du site
print(f'Connecté à SharePoint: {web.properties["Title"]}')
print(f'URL du site: {web.properties["Url"]}')
print(f'ID du site: {web.properties["Id"]}')


   
#Constructing Function for getting file details in SharePoint Folder

def folder_details(ctx, folder_in_sharepoint):
  folder = ctx.web.get_folder_by_server_relative_url(folder_in_sharepoint)
  fold_names = []
  sub_folders = folder.files 
  ctx.load(sub_folders)
  ctx.execute_query()
  for s_folder in sub_folders:
    fold_names.append(s_folder.properties["Name"])
  return fold_names
 
#Getting folder details

file_list = folder_details(ctx, folder_in_sharepoint)

#Printing list of files from sharepoint folder
print(file_list)


def download_files(ctx, folder_url, local_path):
    folder = ctx.web.get_folder_by_server_relative_url(folder_url)
    files = folder.files
    ctx.load(files)
    ctx.execute_query()

    for file in files:
        # Téléchargement du fichier
        download_file(ctx, file.properties["ServerRelativeUrl"], local_path)

        # Chargement des champs de l'élément associé pour accéder aux métadonnées
        list_item = file.listItemAllFields
        ctx.load(list_item)
        ctx.execute_query()

        # Accès sécurisé aux propriétés, avec des valeurs par défaut si non trouvées
        author_name = list_item.properties.get("Author", {}).get("Title", "Inconnu")
        created = list_item.properties.get("Created", "Inconnue")
        modified = list_item.properties.get("Modified", "Inconnue")
        content_type_id = list_item.properties.get("ContentTypeId", "Inconnu")

        # Écriture des métadonnées dans le fichier rapport
        with open('rapportdownload.txt', 'a', encoding='utf-8') as report:
            report.write(f"Nom: {file.properties['Name']}, "
                         f"Propriétaire: {author_name}, Créé le: {created}, Modifié le: {modified}, "
                         f"Type de contenu: {content_type_id}\n")




def download_file(ctx, file_url, local_path):
    response = File.open_binary(ctx, file_url)
    file_name = os.path.basename(file_url)
    with open(os.path.join(local_path, file_name), "wb") as local_file:
        local_file.write(response.content)

# Assurez-vous que le chemin local existe
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Téléchargement des fichiers et écriture des métadonnées
download_files(ctx, folder_in_sharepoint, download_path)

print("Téléchargement terminé. Vérifiez le dossier local et le fichier rapportdownload.txt pour les détails.")



