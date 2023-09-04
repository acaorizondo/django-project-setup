import subprocess
import os
from editSettings import addInstaledAPPS

#-------------------------------------------------------------------------------------------------------------------------------------------------

current_directory = os.path.dirname(os.path.abspath(__file__))
project_name = 'mi_proyecto'
app_name = 'mi_app'

# instalar pipenv si no está instalado
subprocess.run(["pip","install","pipenv"], shell=True)
subprocess.run(['python','--version'], shell=True)

# Instalar Django
subprocess.run(["pipenv", "install", "django"], shell=True)

# activar el entorno virtual
script_bat = 'post_activation.bat'
subprocess.run([script_bat, project_name, app_name], shell=True)

# agregar las alicaciones instaladas al archivo settings.py
project_directory = f"{project_name}\\{project_name}\\settings.py"
new_apps=[f"{app_name}", 'rest_framework']
settings_path = os.path.join(current_directory, project_directory)
addInstaledAPPS(settings_path, new_apps)

# Crear el archivo urls.py en la carpeta de la aplicación
urls_content = "from django.urls import path, include\n\n"
urls_content += "urlpatterns = [\n"
urls_content += "]"

urls_file_path = f"{project_name}\\{app_name}\\urls.py"
urls_path=os.path.join(current_directory, urls_file_path)

with open(urls_path, "w") as urls_file:
    urls_file.write(urls_content)