import random
import os

DJANGO_SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

os.environ['SECRET_KEY'] = DJANGO_SECRET_KEY