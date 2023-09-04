@echo off
setlocal enabledelayedexpansion

rem Obtener los argumentos pasados al archivo .bat
set project_name=%1
set app_name=%2

rem Activa el entorno virtual con "pipenv shell" y ejecuta los comandos dentro de él
mkdir !project_name!
cd !project_name!
pipenv run django-admin startproject !project_name! .
pipenv run python manage.py startapp !app_name!
pipenv run pip install djangorestframework
pipenv run pip install mysqlclient
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

endlocal