import os
os.system('git bisect start')
os.system('git bisect good e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c')
os.system('git bisect bad HEAD')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')