# myscript.py
import os

# Récupère les variables d'environnement
badhash = os.environ.get("BADHASH", "HEAD")
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

os.system("git bisect start $badhash $goodhash")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")