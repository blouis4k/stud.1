from .settings import *  # import everything from your base settings

DEBUG = False

ALLOWED_HOSTS = ['your-subdomain.onrender.com']  # Replace with your actual Render domain

# Static file settings
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Secure headers
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Make sure this is set via Render's environment variables
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Ensure databases are connected securely (Render usually provides this automatically)
