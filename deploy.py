import os
import subprocess

# Set the path to your PythonAnywhere web app directory
web_app_directory = "/home/ashrafabir/ashrafabir.pythonanywhere.com"

# Change to the web app directory
os.chdir(web_app_directory)

# Pull the latest code from your GitHub repository
subprocess.run(["git", "pull"])

# Install dependencies (if using a virtual environment)
subprocess.run(["pip", "install", "-r", "src/requirements.txt"])

# Restart the PythonAnywhere web app
os.system("touch /var/www/ashrafabir_pythonanywhere_com_wsgi.py")
