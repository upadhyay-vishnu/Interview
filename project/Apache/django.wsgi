import os
import sys

sys.path = ['/var/www/myenv/'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'testDRF.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()