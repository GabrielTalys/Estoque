#python3 nome_do_arquivo.py


"""
Django Secret Key Generator
"""
from django.utils.crypto import get_random_string

chars =  'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
DEBUG = True
SECRET_KEY = %s
ALLOWED_HOSTS = 127.0.0.1, .localhost
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=
#EMAIL_USE_TLS=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
""".strip() % get_random_string(50, chars)

#Writing our configuration to '.env'
with open('.env', 'w') as f:
    f.write(CONFIG_STRING)

# Esse script cria um arquivo ".env" com as configurações básicas do Django.
# Ele gera automaticamente uma SECRET_KEY aleatória, usada para manter o site seguro
# (protege logins, senhas e tokens).
#
# Quando usar:
# - Sempre que você iniciar um novo projeto Django e quiser criar rapidamente
#   o arquivo .env com uma chave secreta única.