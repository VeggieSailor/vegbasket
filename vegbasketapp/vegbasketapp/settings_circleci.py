from vegbasketapp.settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'circle_test',
        'USER': 'ubuntu',
        #'PASSWORD': os.environ.get('PG_PASSWORD'),
        'HOST': '127.0.0.1',
    }
}
