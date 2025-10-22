# connexion.py (version corrigée)
import os
import django

# Configurez Django avant d'importer les modèles
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monblog.settings')
django.setup()

# Maintenant vous pouvez importer les modèles Django
from django.db import connection

try:
    cursor = connection.cursor()
    print("✅ Connexion à la base de données réussie!")
except Exception as e:
    print(f"❌ Erreur de connexion: {e}")