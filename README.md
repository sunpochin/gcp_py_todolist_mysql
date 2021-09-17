# gcp_py_todolist_mysql


# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python
# Notes: on Google Cloud Run, has to use main.py instead of application.py, because in example Dockerfile we have: 
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
