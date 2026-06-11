import os
import sys
import shutil
from pathlib import Path

# Add python path for Vercel module resolution
base_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(base_dir))
sys.path.insert(0, str(base_dir.parent))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pulsex.settings')

# Copy database to /tmp on Vercel startup
if os.environ.get('VERCEL') == '1':
    base_dir = Path(__file__).resolve().parent.parent
    src_db = base_dir / 'db.sqlite3'
    dest_db = Path('/tmp/db.sqlite3')
    if src_db.exists() and not dest_db.exists():
        shutil.copy2(src_db, dest_db)


application = get_wsgi_application()

app = application

