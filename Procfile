# Replace example_django with your project root name:
<!-- web: gunicorn bembechat_django.wsgi -->
<!-- web: gunicorn bembechat_django.asgi -->
web: daphne -b 0.0.0.0 -p $5432 bembechat.asgi:application
<!-- web: daphne bembechat_django.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=bembechat_django.settings -v2 -->