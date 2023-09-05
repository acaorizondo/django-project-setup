def addInstaledAPPS(settings_path, new_apps):
    
    # Read the current content of the file
    with open(settings_path, 'r') as file:
        lines = file.readlines()

    # Find the line that contains INSTALLED_APPS
    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if "INSTALLED_APPS" in line:
            start_index = i
            break

    # If INSTALLED_APPS is not found, you may need to handle it differently

    # Find the closing index of the INSTALLED_APPS list (usually contains a ']')
    if start_index is not None:
        for i in range(start_index, len(lines)):
            if ']' in lines[i]:
                end_index = i
                break

    # If the closing of INSTALLED_APPS is not found, you may need to handle it differently

    # Add the new applications after the last application in INSTALLED_APPS
    if start_index is not None and end_index is not None:
        #lines[end_index] = lines[end_index].replace(']', ',')  # Add a comma at the end of the last application
        for app in new_apps:
            lines.insert(end_index, f"    '{app}',\n")  # Add the new applications
        lines[end_index + len(new_apps)] = lines[end_index + len(new_apps)].rstrip(',') + '\n'  # Remove the comma from the last added application

    # Write the modified content back to the file
    with open(settings_path, 'w') as file:
        file.writelines(lines)
        
def updateStatics(settings_path, apps):
    # Read the current content of the file
    with open(settings_path, 'r') as file:
        lines = file.readlines()

    # Find the line that contains INSTALLED_APPS
    start_index = None

    for i, line in enumerate(lines):
        if "STATIC_URL" in line:
            start_index = i
            break
    
    # add STATICFILES_DIRS
    if start_index is not None:
       
        i=1
        lines.insert(start_index+i, f"STATICFILES_DIRS = [\n")  # Add staticfiles_dir
        for app in apps:
            i+=1
            lines.insert(start_index+i, f"    '{app}/static',\n")  # Add staticfiles_dir
        lines.insert(start_index+i+1, f"]\n")  # Add staticfiles_dir
    
    # Write the modified content back to the file
    with open(settings_path, 'w') as file:
        file.writelines(lines)

def updateTemplatesDir(settings_path, template_dir):
    # Read the current content of the file
    with open(settings_path, 'r') as file:
        lines = file.readlines()

    # Find the line that contains INSTALLED_APPS
    start_index = None

    for i, line in enumerate(lines):
        if "'BACKEND': 'django.template.backends.django.DjangoTemplates'," in line:
            start_index = i+1
            break
    
    # add STATICFILES_DIRS
    if start_index is not None:
        lines.pop(start_index)
        lines.insert(start_index, f"        'DIRS': ['{template_dir}/templates', '/templates'],\n")
    
    # Write the modified content back to the file
    with open(settings_path, 'w') as file:
        file.writelines(lines)
    