CONFIG = {
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=4',
        '--pythonpath=/home/box/web',
        'hello:wsgi_application',
    ),
}