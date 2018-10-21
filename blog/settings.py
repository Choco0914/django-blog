import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y$a)3faq3*h#r0g5b^cxsw^lgdxbbu&#lsqek!_0ju+d*c!ups'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 내가 만든 앱
    'my_blog',
    #USER APP
    'users',

    # Apps created by others
    'bootstrap3',

    # Restful api Framework
    'rest_framework',
    # Social
    'social_django',
    "social_core",

    # customize form
    'widget_tweaks',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 내 설정
LOGIN_URL = '/users/login/'

# django-bootstrap3 settings
BOOTSTRAP3 = {
    'include_jquery' : True,
}

#  Heroku settings

cwd = os.getcwd()
if cwd == '/app' or cwd[:4] == '/tmp':
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost')
    }

    # request.is_secure()에 대해 'X-Forwarded-Proto'를 우선적으로 사용한다.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # 모든 호스트 헤더를 허용한다.
    ALLOWED_HOSTS = ['choco-blog.herokuapp.com']

    DEBUG = False

    # Static asset configuration
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    # Verification Email settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = 'True'
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'heojeongho1992@gmail.com'
    EMAIL_HOST_PASSWORD = os.environ.get('KBOARD_PASSWORD')
    SERVER_EMAIL = 'heojeongho1992@gmail.com'
    DEFAULT_FROM_MAIL = 'my_blog'

# AUTHENTICATION_BACKENDS settings
AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2', # for Github authentication
    'social_core.backends.kakao.KakaoOAuth2', # for Kakaotlak authentication

    'django.contrib.auth.backends.ModelBackend', # Django 기본 유저모델
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
LOGIN_REDIRECT_URL='/'

# Google login
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='843562355161-3atsmmageh4j0758g4am6e4ncefckupf.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='ZVKObQDFPhTdz1GXWfaYuulq'
# Github Login
SOCIAL_AUTH_GITHUB_KEY = 'e2fc4a9cf1f213b0a10f'
SOCIAL_AUTH_GITHUB_SECRET = 'c4d1efe407175230a47d7fa547db0667b4f08721'

# Kakaotalk login
SOCIAL_AUTH_KAKAO_KEY = '490c43bc63dd3351e6068f6bbf4e0bfd'

# Verification Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = 'True'
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'heojeongho1992@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('KBOARD_PASSWORD')
SERVER_EMAIL = 'heojeongho1992@gmail.com'
DEFAULT_FROM_MAIL = 'my_blog'
