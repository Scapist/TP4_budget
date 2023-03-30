import os
os.system('git bisect start')
os.system('git bisect bad')
os.system('git checkout e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c')
os.system('git bisect good')
os.system('git bisect run python manage.py test')