import subprocess
import os
from editSettings import addInstaledAPPS, updateStatics, updateTemplatesDir
from editUrls import  createAppUrls, editProjectUrls

#-------------------------------------------------------------------------------------------------------------------------------------------------

current_directory = os.path.dirname(os.path.abspath(__file__))
project_name = 'my_project'
app_name = 'my_app'

# instalar pipenv si no está instalado
subprocess.run(["pip","install","pipenv"], shell=True)
subprocess.run(['python','--version'], shell=True)

# Instalar Django
subprocess.run(["pipenv", "install", "django"], shell=True)

# activar el entorno virtual, crear proyecto django y aplicación, 
# instalar django rest framework, ejecutar migraciones, crear templates y statics folders
script_bat = 'post_activation.bat'
subprocess.run([script_bat, project_name, app_name], shell=True)

# agregar las alicaciones instaladas al archivo settings.py
project_directory = f"{project_name}\\{project_name}\\settings.py"
new_apps=[f"{app_name}", 'rest_framework']
settings_path = os.path.join(current_directory, project_directory)
addInstaledAPPS(settings_path, new_apps)

# agregar las direcciones de los archivos estáticos
statics_dirs=[app_name]
updateStatics(settings_path, statics_dirs)

# agregar las ubicaciones de los templates
updateTemplatesDir(settings_path, app_name)

# Crear el archivo urls.py en la carpeta de la aplicación
createAppUrls(project_name, app_name, current_directory)

# Añadir la ruta a las urls de la aplicación en el proyecto
editProjectUrls(project_name, app_name, current_directory)