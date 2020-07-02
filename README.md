## Description

DEPRECATED!

Strips leading and trailing whitespace from response content in Django application.

## Installing

```bash
$ pip install -e git://github.com/eugena/django-stripwhitespace-middleware.git#egg=django-stripwhitespace-middleware
```

Then add ```django_stripwhitespace_middleware.middleware.StripWhitespaceMiddleware``` to the end your ```MIDDLEWARE_CLASSES```.

For example:

```
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
    'django_stripwhitespace_middleware.middleware.StripWhitespaceMiddleware'
)
```

Enjoy.
