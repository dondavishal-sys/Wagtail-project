import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings.production")

from django.core.wsgi import get_wsgi_application

# Auto-create superuser on startup
try:
    from startup_superuser import create_superuser
    create_superuser()
except Exception as e:
    print(f"Superuser creation skipped: {e}")

application = get_wsgi_application()
