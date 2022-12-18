#
# Django项目的最小Docker映像
#
FROM python:3.7

# 确保Python输出应用程序内打印的所有内容，而不是缓冲它。
ENV PYTHONUNBUFFERED 1

# 安装 PostgreSQL 客户端
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql-client

# 设置默认目录
WORKDIR /app

COPY . /app/

RUN pip install -r /app/requirements/base.txt \
    && pip install -r /app/requirements/test.txt

RUN python manage.py makemigrations \
    && python manage.py migrate

