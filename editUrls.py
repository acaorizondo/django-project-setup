import os
# Crear el archivo urls.py en la carpeta de la aplicación
def createAppUrls(project_name, app_name, current_directory):
    urls_content = "from django.urls import path, include\n\n"
    urls_content += "urlpatterns = [\n"
    urls_content += "]"

    urls_file_path = f"{project_name}\\{app_name}\\urls.py"
    urls_path=os.path.join(current_directory, urls_file_path)

    with open(urls_path, "w") as urls_file:
        urls_file.write(urls_content)

# edita el archivo urls.py del proyecto        
def editProjectUrls(project_name, app_name, current_directory):
    urls_file_path = f"{project_name}\\{project_name}\\urls.py"
    urls_path=os.path.join(current_directory, urls_file_path)
    
    # Read the current content of the file
    with open(urls_path, 'r') as file:
        lines = file.readlines()

    # Find the line that contains INSTALLED_APPS
    start_index = None

    for i, line in enumerate(lines):
        if "from django.urls import path" in line:
            import_index = i
        if "path('admin/', admin.site.urls)," in line:
            paths_index = i
            break
        
    if import_index is not None:
        i=1
        lines.insert(import_index+i, f"from django.urls import include\n")
    
    if paths_index is not None:
        i=1
        lines.insert(paths_index+i, f" path('{app_name}/', include('{app_name}.urls')),\n")
        
    # Write the modified content back to the file
    with open(urls_path, 'w') as file:
        file.writelines(lines)