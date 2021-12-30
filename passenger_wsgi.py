import sys, os
from pathlib import Path

sys.path.append(Path(__file__).resolve().parent.__str__() + '/venv/lib/python3.7/site-packages')

from djangoProject.wsgi import application
