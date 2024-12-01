import sys
import os
import django

sys.path.append('/home/user12/Project/work/doctifycom_project')

os.environ['DJANGO_SETTINGS_MODULE'] = 'doctifycom_project.settings'
django.setup()