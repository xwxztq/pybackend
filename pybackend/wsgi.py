"""
WSGI config for pybackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pybackend.settings')

cur_pwd = os.getcwd()

w2m = os.path.join(cur_pwd,"wav2mids","w2m")
climax = os.path.join(cur_pwd,"climax4musics","climax")
genre = os.path.join(cur_pwd,"genre4musics","genres")

sys.path.append(w2m)
sys.path.append(climax)
sys.path.append(genre)

print(sys.path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pybackend.settings")

application = get_wsgi_application()
