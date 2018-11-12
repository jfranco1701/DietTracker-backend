# Set to DEV for debug and other configuration items.  PROD otherwise...
ENVIRONMENT = 'DEV'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9nzh^gu^c^q0-e9bw4m)i4q82*q!44*ssivk5f@fibd(x+zd-1'

#ROOT_URLCONF = 'urls'
ROOT_URLCONF = 'django_backend.urls'
WSGI_APPLICATION = 'django_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
