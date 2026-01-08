from pathlib import Path
import os
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-kunci-rahasia-skripsi-anda'
DEBUG = True
#DEBUG = os.environ.get('VERCEL') is None
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh']

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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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

# --- KONFIGURASI DATABASE MYSQL (XAMPP) ---
# PERBAIKAN: Jika error "MariaDB 10.5 required", coba tambahkan OPTIONS
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'db_sekolah_skripsi',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': '127.0.0.1',
#         'PORT': '3309',
#         'OPTIONS': {
#             # Opsi ini membantu kompatibilitas
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#             'charset': 'utf8mb4',
#         },
#     }
# }

if 'VERCEL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse("npx neonctl@latest init")
    }
else:
    # Database Lokal (Tetap SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

LOGIN_REDIRECT_URL = 'home' 

# Setelah logout, arahkan kembali ke homepage
LOGOUT_REDIRECT_URL = 'home'

# Halaman login ada di URL ini (jika user akses halaman yg diproteksi)
LOGIN_URL = 'login'
# --- SOLUSI ALTERNATIF JIKA MYSQL MASIH ERROR ---
# Jika MySQL XAMPP Anda terlalu tua dan error terus,
# Hapus bagian DATABASES di atas, dan pakai SQLite ini (Hapus tanda pagar #):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


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

# STATIC_URL = 'static/'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Folder tempat kita menaruh CSS/JS kustom kita sendiri (selain admin)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Gunakan WhiteNoise untuk melayani file statis di Vercel
# CompressedManifestStaticFilesStorage membuat file lebih kecil & cacheable
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- MEDIA FILES (Upload Foto) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')