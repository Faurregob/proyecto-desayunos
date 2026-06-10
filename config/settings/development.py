from .base import *

# ==============================================================================
# DESARROLLO — Estas configuraciones NUNCA deben llegar a producción
# ==============================================================================

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# En desarrollo usamos la consola para ver los emails enviados
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'