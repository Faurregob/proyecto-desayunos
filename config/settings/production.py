from .base import *

# ==============================================================================
# PRODUCCIÓN — Configuraciones de seguridad estrictas
# ==============================================================================

DEBUG = False

# En producción los hosts vienen de variable de entorno
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Seguridad HTTPS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'