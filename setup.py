from distutils.core import setup

setup(
    name = 'django-stripwhitespace-middleware',
    packages = ['django_stripwhitespace_middleware'],
    license = 'MIT',
    version = '0.1',
    description = 'Strips leading and trailing whitespace from django response content.',
    author = 'Eugena Mihailikova',
    author_email = 'eugena.mihailikova@gmail.com',
    url = 'https://github.com/eugena/django-stripwhitespace-middleware/',
    download_url = 'https://github.com/eugena/django-stripwhitespace-middleware/tarball/0.1',
    keywords = ['django','middleware','response', 'strips whitespace', ],
    classifiers = [],
)