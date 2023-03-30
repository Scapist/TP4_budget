import os
os.system('git bisect start HEAD master')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')