from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

# Paramètres de connexion
#username = 'votre_email@votredomaine.com'
#password = 'votre_mot_de_passe'
username = 'souleysanogo@gs2e.ci'
password = 'forHAKIM78'

#site_name = 'nom_du_site'
#base_url = 'https://votredomaine.sharepoint.com'   
#site_url = base_url + '/sites/' + site_name
base_url = 'https://ciesodecigs2e.sharepoint.com'  
site_url = 'https://ciesodecigs2e.sharepoint.com/dri'

#https://ciesodecigs2e.sharepoint.com/dri/Documents%20partages/CCDC

# Chemin du dossier à lister (par exemple, "Documents partagés/MonDossier")
# Remplacer 'MonDossier' par le nom du dossier que vous souhaitez lister
folder_path = '/Documents%20partages/CCDC'

# Authentification
authcookie = Office365(base_url, username=username, password=password).GetCookies()
site = Site(site_url, version=Version.v365, authcookie=authcookie)

# Accès au dossier racine du site
folder = site.Folder('.')

# Lister les fichiers à la racine
files = folder.files
for file in files:
    print(file['Name'])

