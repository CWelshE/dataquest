# djangocker coderunner
Another website code runner written in Django. Uses Docker instances.

# Architecture
Using an ACE editor (the same one GitHub uses for online edits), this application lets a user submit Python code online.
It is then fed to Django, which spins up a Docker instance and runs said code.

Docker will then feed stdout to Django, which gets posted back to the virtual terminal.

# Setting Up

As this is a demonstration, you will need to do these things:

* python manage.py runserver
* docker daemon
* docker build -t cr (inside of the main directory)
* make sure your path is correctly represented so that Docker mounts code.py

Then, navigate to 127.0.0.1:8000/codeparser to see the project.
