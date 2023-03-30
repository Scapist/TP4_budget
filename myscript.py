import os
os.system('git bisect start')
os.system('git bisect bad')
os.system('git bisect start HEAD~2')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')