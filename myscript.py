import os
os.system('git bisect start')
os.system('git checkout main')
os.system('git bisect bad')
os.system('git checkout good-branch')
os.system('git bisect good')
os.system('git bisect run python manage.py test')