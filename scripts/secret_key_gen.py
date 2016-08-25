import random
import os

DJANGO_SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

with open(os.path.expanduser('~/.bash_profile'), 'a') as outfile:
    outfile.write('export SECRET_KEY=' + repr(DJANGO_SECRET_KEY))