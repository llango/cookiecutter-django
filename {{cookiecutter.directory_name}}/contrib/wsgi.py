"""
项目 {{cookiecutter.project_slug}} 的WSGI配置
它将可调用的WSGI公开为名为“application”的模块级变量。
可以点击连接查看文档了解更多
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

app_path = os.path.abspath(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(os.path.join(app_path, "{{ cookiecutter.project_slug }}"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.project_slug}}.settings')

application = get_wsgi_application()