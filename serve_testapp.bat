cd C:\Users\wl239\PycharmProjects\testapp
git pull https://%TESTAPP_GIT_PAT%@github.com/wl239/testapp.git
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe server.py