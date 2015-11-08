# djangocker coderunner
Another website code runner written in Django. Uses Docker instances.

# Architecture
Using an ACE editor (the same one GitHub uses for online edits), this application lets a user submit Python code online.
It is then fed to Django, which spins up a Docker instance and runs said code.

Docker will then feed stdout to Django, which gets posted back to the virtual terminal.
