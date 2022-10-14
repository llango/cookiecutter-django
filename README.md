Cookiecutter Django 
================================
高效快速开始你的Django项目。

依赖
-----------

- Docker / Docker-compose
- Python 3.7

使用
-----

首先，创建并激活你的虚拟环境。

安装 cookiecutter 并设置项目： 

```bash
pip install cookiecutter
cookiecutter https://github.com/llango/cookiecutter-django -f -o ..
```

设置首个配置：

```bash
pip install -r requirements-test.txt
cp -r env-sample .env
```

命令
-------

运行 postgresql 和 redis:
```bash
make docker-compose-up
```

运行 django 开发服务器：
```bash
make dev
```

运行测试:
```bash
make test
```

下一步
-----

- [ ] 完善改cookiecutter。
- [ ] 添加部署说明文档。


