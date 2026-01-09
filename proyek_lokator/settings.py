from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-kunci-rahasia-skripsi-anda'
DEBUG = True
# DEBUG = os.environ.get('VERCEL') is None # Bisa diaktifkan nanti untuk production
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'locator',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Wajib untuk Vercel
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyek_lokator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyek_lokator.wsgi.application'

# --- KONFIGURASI DATABASE CERDAS (PostgreSQL / SQLite) ---

# Cek apakah ada environment variable DATABASE_URL (biasanya dari Neon/Vercel)
database_url = os.environ.get('DATABASE_URL')

if database_url and database_url.startswith("postgres"):
    # Jika ada link PostgreSQL yang valid, gunakan itu
    DATABASES = {
        'default': dj_database_url.config(default=database_url)
    }
else:
    # Jika TIDAK ADA link PostgreSQL (atau kosong), gunakan SQLite
    # Ini aman untuk lokal DAN demo Vercel tanpa Neon
    
    if 'VERCEL' in os.environ:
        # Di Vercel, kita harus menggunakan folder /tmp karena folder lain read-only
        # Script build_files.sh akan membuat/memigrasi database di sini
        db_path = '/tmp/db.sqlite3'
    else:
        # Di Laptop, gunakan folder proyek biasa
        db_path = BASE_DIR / 'db.sqlite3'
        
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': db_path,
        }
    }

# --- KONFIGURASI LOGIN ---
LOGIN_REDIRECT_URL = 'home' 
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]